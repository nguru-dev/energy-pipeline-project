provider "aws" {
  region = "us-east-2"
}

# Lambda Function
resource "aws_lambda_function" "energy_processor" {
  function_name = "ProcessEnergyData"
  role          = "arn:aws:iam::919313849757:role/ProcessEnergyData-role-iwqhswuu"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  timeout       = 10

  filename         = "${path.module}/../lambda_function.zip"
  source_code_hash = filebase64sha256("${path.module}/../lambda_function.zip")

  lifecycle {
    ignore_changes = [role, handler, runtime, timeout]
  }
}

# S3 → Lambda Trigger Permission
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.energy_processor.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::energy-data-bucket-guru"
}

# S3 Trigger Configuration
resource "aws_s3_bucket_notification" "s3_trigger" {
  bucket = "energy-data-bucket-guru"

  lambda_function {
    lambda_function_arn = aws_lambda_function.energy_processor.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "raw/"
    filter_suffix       = ".json"
  }

  depends_on = [aws_lambda_permission.allow_s3]
}

# SNS Topic for Anomalies
resource "aws_sns_topic" "anomaly_alerts" {
  name = "anomaly-alerts"
}

# Email Subscription
resource "aws_sns_topic_subscription" "email_alert" {
  topic_arn = aws_sns_topic.anomaly_alerts.arn
  protocol  = "email"
  endpoint  = "gurusai2122@gmail.com"
}

# IAM Role (imported, so protect it)
resource "aws_iam_role" "lambda_exec_role" {
  name = "ProcessEnergyData-role-iwqhswuu"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })

  lifecycle {
    prevent_destroy = true
    ignore_changes  = all
  }
}

# SNS Full Access for Lambda Role
resource "aws_iam_policy_attachment" "sns_publish_access" {
  name       = "lambda_sns_publish"
  roles      = [aws_iam_role.lambda_exec_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonSNSFullAccess"
}
