output "cloudfront_route53_alias" {
  description = "The route53 CloudFront alias."

  value = local.domain
}