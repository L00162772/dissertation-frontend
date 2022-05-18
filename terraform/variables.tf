variable "aws_region" {
  type    = string
  default = "###AWS_REGION###"
}
variable "terraform_cloud_organisation" {
  type    = string
  default = "dissertation"
}
variable "terraform_cloud_workspace" {
  type    = string
  default = "###TERRAFORM_CLOUD_WORKSPACE###"
}
variable "bucket_name_postfix" {
  default     = "l00162772-frontend"
  description = "The name of the bucket for the frontend code"
}

variable "route53_domain" {
  default     = "atu-dissertation.com"
  description = "Domain to deploy the application at"
}
