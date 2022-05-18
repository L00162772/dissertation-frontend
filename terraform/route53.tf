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

resource "aws_route53_record" "cloudfront_frontend" {
  zone_id = data.aws_route53_zone.frontend_route53.zone_id
  name    = "${var.aws_region}-cloudfront-frontend"
  type    = "CNAME"
  ttl     = "5"

  records = [aws_cloudfront_distribution.frontend_cloudfront_distribution.domain_name]
}

resource "aws_route53_record" "alb_frontend" {
  zone_id = data.aws_route53_zone.frontend_route53.zone_id
  name    = "${var.aws_region}-alb-frontend"
  type    = "A"

  alias {
    name                   = aws_lb.frontend_alb.dns_name
    zone_id                = aws_lb.frontend_alb.zone_id
    evaluate_target_health = true
  }

  depends_on = [
    aws_lb.frontend_alb
  ]
}

resource "aws_route53_record" "frontend" {
  zone_id = data.aws_route53_zone.frontend_route53.zone_id
  name    = "frontend"
  type    = "A"

  alias {
    name                   = aws_globalaccelerator_listener.frontend_global_accelerator.dns_name
    zone_id                = aws_globalaccelerator_listener.frontend_global_accelerator.zone_id
    evaluate_target_health = true
  }

  depends_on = [
    aws_globalaccelerator_listeneraws_lb.frontend_global_accelerator
  ]
}