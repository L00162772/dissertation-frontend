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
  bucket = "${var.aws_region}-${var.bucket_name_postfix}"
  acl    = "public-read"
  policy = data.aws_iam_policy_document.s3-website-policy.json
  website {
    index_document = "index.html"
    error_document = "index.html"
  }
  force_destroy = true
}
resource "aws_s3_bucket_public_access_block" "frontend_s3_access_control" {
  bucket             = aws_s3_bucket.frontend_s3_bucket.id
  block_public_acls  = true
  ignore_public_acls = true
}
