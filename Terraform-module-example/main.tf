terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

module "NetInfra" {
  source = "./NetInfra"
}

module "WebAppsAndStorage" {
  source = "./WebAppsAndStorage"
  target_vpc_id = module.NetInfra.vpc_id
  target_subnet_id = module.NetInfra.subnet_id
}