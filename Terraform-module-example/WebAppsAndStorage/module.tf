variable "target_vpc_id" {
  type        = string
  description = "The VPC ID passed from the VPC module"
}

variable "target_subnet_id" {
  type        = string
  description = "The subnet ID passed from the VPC module"
}

resource "aws_s3_bucket" "S3" {
  bucket = "s3-logo-bucket-67c3ca20-7f21-4f6e-915f-33c94d0e6530"
  tags = {
    Name = "The bucket"
  }
}

resource "aws_s3_object" "logo_upload" {
  bucket = aws_s3_bucket.S3.id
  key    = "logo.png"
  source = "./logo/logo.png"
  content_type = "image/png"
  etag = filemd5("./logo/logo.png")
}

resource "aws_efs_file_system" "efs_resource" {
  creation_token = "my-efs"

  tags = {
    Name = "MyEFS"
  }
}


resource "aws_security_group" "web_servers_sg" {
  name        = "web-servers-sg"
  vpc_id      = var.target_vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "efs_sg" {
  name        = "efs-storage-sg"
  vpc_id      = var.target_vpc_id

  ingress {
    from_port       = 2049
    to_port         = 2049
    protocol        = "tcp"
    security_groups = [aws_security_group.web_servers_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_efs_mount_target" "mounting_point" {
  file_system_id = aws_efs_file_system.efs_resource.id
  subnet_id      = var.target_subnet_id
  security_groups = [aws_security_group.efs_sg.id]
}


resource "aws_iam_role" "ec2_s3_access_role" {
  name = "ec2-s3-access-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy_attachment" "s3_readonly" {
  role       = aws_iam_role.ec2_s3_access_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ec2-s3-instance-profile"
  role = aws_iam_role.ec2_s3_access_role.name
}


resource "aws_instance" "web_app_server" {
  ami                    = "ami-0c101f26f147fa7fd" # Amazon Linux 2023
  instance_type          = "t2.micro"
  subnet_id              = var.target_subnet_id
  vpc_security_group_ids = [aws_security_group.web_servers_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name
  depends_on = [aws_efs_mount_target.mounting_point]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y amazon-efs-utils python3-botocore docker
              systemctl start docker
              systemctl enable docker

              # 2. Setup EFS Mount Point
              mkdir -p /mnt/efs
              # Mount the EFS (Using the EFS ID from your other resource)
              mount -t efs -o tls ${aws_efs_file_system.efs_resource.id}:/ /mnt/efs

              # 3. Pull Logo from S3 to EFS
              aws s3 cp s3://${aws_s3_bucket.S3.id}/logo.png /mnt/efs/logo.png

              # 4. Create the Index.html on the EFS
              cat <<HTML > /mnt/efs/index.html
              <!DOCTYPE html>
              <html>
              <head>
                  <title>Welcome to my App</title>
                  <style>
                      body { font-family: sans-serif; text-align: center; padding-top: 50px; }
                      img { max-width: 300px; }
                  </style>
              </head>
              <body>
                  <h1>Hello from EC2 & EFS!</h1>
                  <img src="logo.png" alt="Company Logo">
                  <p>This page and the logo above are being served from a shared EFS volume.</p>
              </body>
              </html>
              HTML

              # 5. Run Nginx Container
              # -v /mnt/efs:/usr/share/nginx/html maps your EFS to Nginx's web root
              docker run -d -p 80:80 --name web-server -v /mnt/efs:/usr/share/nginx/html:ro nginx
              EOF

  tags = {
    Name = "Web-App-Instance"
  }
}

resource "aws_instance" "apache_server" {
  ami                    = "ami-0c101f26f147fa7fd" # Amazon Linux 2023
  instance_type          = "t2.micro"
  subnet_id              = var.target_subnet_id
  vpc_security_group_ids = [aws_security_group.web_servers_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name
  depends_on = [aws_efs_mount_target.mounting_point]
  
  user_data = <<-EOF
              #!/bin/bash
              # 1. Install EFS tools and Docker
              yum update -y
              yum install -y amazon-efs-utils python3-botocore docker
              systemctl start docker
              systemctl enable docker

              # 2. Setup EFS Mount Point
              mkdir -p /mnt/efs
              # Mount the existing EFS
              mount -t efs -o tls ${aws_efs_file_system.efs_resource.id}:/ /mnt/efs

              # 3. Run Apache (httpd) Container
              # Mapping the EFS to Apache's default htdocs folder
              docker run -d -p 80:80 --name apache-server -v /mnt/efs:/usr/local/apache2/htdocs/:ro httpd
              EOF

  tags = {
    Name = "Apache-EFS-Reader"
  }
}
