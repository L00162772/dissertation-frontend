output "cloudfront_route53_alias" {
  description = "The route53 CloudFront alias."

  value = local.cloudfront_domain
}

output "cloudfront_distribution_id" {
  description = "The CloudFront distribution id."

  value = aws_cloudfront_distribution.frontend_cloudfront_distribution.id
}

output "alb_dns_name" {
  value = aws_lb.frontend_alb.dns_name
}