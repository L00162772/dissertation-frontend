data "aws_iam_policy_document" "s3-website-policy" {
  statement {
    actions = [
      "s3:GetObject"
    ]
    principals {
      identifiers = ["*"]
      type        = "AWS"
    }
    resources = [
      "arn:aws:s3:::${var.aws_region}-${var.bucket_name_postfix}/*"
    ]
  }
}

resource "aws_s3_bucket" "frontend_s3_bucket" {
  bucket        = "${var.aws_region}-${var.bucket_name_postfix}"
  force_destroy = true
}

resource "aws_s3_bucket_acl" "frontend_s3_bucket_acl" {
  bucket = aws_s3_bucket.exfrontend_s3_bucketmple.id
  acl    = "public-read"
}

resource "aws_s3_bucket_website_configuration" "frontend_s3_bucket_configuration" {
  bucket = aws_s3_bucket.frontend_s3_bucket.bucket

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "index.html"
  }
}

resource "aws_s3_bucket_public_access_block" "frontend_s3_access_control" {
  bucket             = aws_s3_bucket.frontend_s3_bucket.id
  block_public_acls  = true
  ignore_public_acls = true
}

resource "aws_s3_bucket_policy" "frontend_s3_bucket_policy" {
  bucket = aws_s3_bucket.frontend_s3_bucket.id
  policy = data.aws_iam_policy_document.s3-website-policy.json
}


