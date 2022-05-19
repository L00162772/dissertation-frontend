
resource "aws_cloudfront_distribution" "frontend_cloudfront_distribution" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "The cloudfront distribution for the ${var.aws_region} frontend deployment"
  default_root_object = "index.html"
  aliases             = [local.cloudfront_domain]
  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = local.s3_origin_id
    viewer_protocol_policy = "redirect-to-https"
    forwarded_values {
      query_string = false
      cookies {
        forward = "all"
      }
    }
  }
  origin {
    domain_name = aws_s3_bucket.frontend_s3_bucket.bucket_regional_domain_name
    origin_id   = local.s3_origin_id
  }
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
  viewer_certificate {
    acm_certificate_arn = aws_acm_certificate.frontend_cloudfront_cert.arn
    ssl_support_method  = "sni-only"
  }
  custom_error_response {
    error_code            = 404
    error_caching_min_ttl = 86400
    response_page_path    = "/index.html"
    response_code         = 200
  }
  depends_on = [
    aws_acm_certificate_validation.cloudfront_cert_validation
  ]
}