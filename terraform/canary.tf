
resource "aws_iam_role" "canary_role" {
  name = "canary_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_s3_bucket" "frontend_canary_s3_bucket" {
  bucket        = "${var.aws_region}-canary-${var.bucket_name_postfix}"
  force_destroy = true
}
resource "aws_s3_bucket_acl" "frontend_canary_s3_bucket_acl" {
  bucket = aws_s3_bucket.frontend_canary_s3_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "frontend_canary_s3_access_control" {
  bucket             = aws_s3_bucket.frontend_canary_s3_bucket.id
  block_public_acls  = true
  ignore_public_acls = true
}

# Zip the Lamda function on the fly
data "archive_file" "zip_frontend_canary_lambda" {
  type        = "zip"
  source_dir  = "canaries/forgot_password.py"
  output_path = "canaries/forgot_password.zip"
}

# Upload canary file to S3
resource "aws_s3_object" "frontend_canary_lambda" {
  bucket = aws_s3_bucket.frontend_canary_s3_bucket.id
  key    = "forgot_password.zip"
  source = data.archive_file.zip_frontend_canary_lambda.output_path
  etag   = filemd5(data.archive_file.zip_frontend_canary_lambda.output_path)
  depends_on = [
    data.archive_file.zip_frontend_canary_lambda
  ]
}

resource "aws_synthetics_canary" "frontend_canary" {
  name                 = "frontend_canary"
  artifact_s3_location = "s3://${aws_s3_bucket.frontend_canary_s3_bucket.id}"
  execution_role_arn   = aws_iam_role.frontend-canary-role.arn
  runtime_version      = "syn-python-selenium-1.0"
  handler              = "forgot_password.handler"
  s3_bucket            = aws_s3_bucket.frontend_canary_s3_bucket.id
  s3_key               = "forgot_password.zip"
  start_canary         = true

  success_retention_period = 2
  failure_retention_period = 14

  schedule {
    expression          = "rate(1 minute)"
    duration_in_seconds = 0
  }

  run_config {
    timeout_in_seconds = 60
    memory_in_mb       = 960
    active_tracing     = false
  }
  depends_on = [
    aws_s3_object.frontend_canary_lambda
  ]
}

data "aws_iam_policy_document" "frontend-canary-assume-role-policy" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
  }
}

resource "aws_iam_role" "frontend-canary-role" {
  name               = "frontend-canary-role"
  assume_role_policy = data.aws_iam_policy_document.frontend-canary-assume-role-policy.json
  description        = "IAM role for AWS Synthetic Monitoring Frontend Canaries"
}

data "aws_iam_policy_document" "frontend-canary-policy" {
  statement {
    sid    = "CanaryGeneric"
    effect = "Allow"
    actions = [
      "s3:PutObject",
      "s3:GetBucketLocation",
      "s3:ListAllMyBuckets",
      "cloudwatch:PutMetricData",
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "frontend-canary-policy" {
  name        = "frontend-canary-policy"
  policy      = data.aws_iam_policy_document.frontend-canary-policy.json
  description = "IAM role for AWS Synthetic Monitoring Frontend Canaries"
}

resource "aws_iam_role_policy_attachment" "frontend-canary-policy-attachment" {
  role       = aws_iam_role.frontend-canary-role.name
  policy_arn = aws_iam_policy.frontend-canary-policy.arn
}