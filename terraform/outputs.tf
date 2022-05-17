output "cloudfront_route53_alias" {
  description = "The route53 CloudFront alias."

  value = local.domain
}

output "cloudfront_distribution_id" {
  description = "The CloudFront distribution id."

  value = aws_cloudfront_distribution.frontend_cloudfront_distribution.id
}