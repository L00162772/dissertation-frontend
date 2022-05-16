# Note SSL certs can only be created in this region
resource "aws_acm_certificate" "frontend_cloudfront_cert" {
  provider          = aws.east1
  domain_name       = local.domain
  validation_method = "DNS"
  lifecycle {
    create_before_destroy = true
  }
}



resource "aws_acm_certificate_validation" "validation" {
  certificate_arn   = aws_acm_certificate.frontend_cloudfront_cert.arn
  provider          = aws.east1
  validation_record_fqdns = [for record in aws_route53_record.frontend_cloudfront_route53_validation_record : record.fqdn]
  depends_on = [
    aws_route53_record.frontend_cloudfront_route53_validation_record
  ]
}