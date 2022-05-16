resource "aws_iam_policy" "cloudfront-invalidate-paths" {
  name        = "cloudfront-invalidate-paths"
  description = "Used by CI pipelines to delete cached paths"
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid      = "VisualEditor0",
        Effect   = "Allow",
        Action   = "cloudfront:CreateInvalidation",
        Resource = "*"
      }
    ]
  })
}