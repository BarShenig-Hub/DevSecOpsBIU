resource "aws_vpc" "web_app" {
  cidr_block       = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  instance_tenancy = "default"

  tags = {
    Name = "VPC-Web-App"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.web_app.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "Public Subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.web_app.id
  tags = {
    Name = "IGW"
  }
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_route_table.id
}

resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.web_app.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "Public Route Table"
  }
}

output "vpc_id" {
  value       = aws_vpc.web_app.id
  description = "The ID of the VPC"
}

output "subnet_id" {
  value       = aws_subnet.public_subnet.id
  description = "The ID of the subnet"
}

