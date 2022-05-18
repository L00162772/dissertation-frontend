

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.14.0"
    }
  }
  required_version = ">= 1.1.9"

  backend "remote" {
    organization = var.terraform_cloud_organisation

    workspaces {
      name = var.terraform_cloud_workspace
    }
  }
}


data "aws_caller_identity" "current" {}
provider "aws" {
  region = var.aws_region
  #profile = "lyit"
  default_tags {
    tags = {
      Region = var.aws_region
      Name   = "frontend"
    }
  }
}
provider "aws" {
  region = "us-east-1"
  alias  = "east1"
  #profile = "lyit"
}
locals {
  domain       = "${var.aws_region}-frontend.${var.route53_domain}"
  s3_origin_id = "${var.aws_region}-frontend-s3-origin"
}
