data "aws_route53_zone" "frontend_route53" {
  name         = var.route53_domain
  private_zone = false
}

resource "aws_route53_record" "frontend_cloudfront_route53_validation_record" {
  for_each = {
    for dvo in aws_acm_certificate.frontend_cloudfront_cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.frontend_route53.zone_id
  depends_on = [
    aws_acm_certificate.frontend_cloudfront_cert
  ]
}

resource "aws_route53_record" "frontend" {
  zone_id = data.aws_route53_zone.frontend_route53.zone_id
  name    = "${var.aws_region}-frontend"
  type    = "CNAME"
  ttl     = "5"


  records = [aws_cloudfront_distribution.frontend_cloudfront_distribution.domain_name]
}