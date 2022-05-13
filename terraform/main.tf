provider "aws" {
  region = var.aws_region
  profile = "lyit"
}
provider "aws" {
  region = "us-east-1"
  alias  = "east1"
  profile = "lyit"
}
locals {
  domain       = "${var.aws_region}-frontend.${var.route53_domain}"
  s3_origin_id = "${var.aws_region}-frontend-s3-origin"
}
