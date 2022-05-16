variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "bucket_name_postfix" {
  default     = "l00162772-frontend"
  description = "The name of the bucket for the frontend code"
}

variable "route53_domain" {
  default     = "atu-dissertation.com"
  description = "Domain to deploy the application at"
}
