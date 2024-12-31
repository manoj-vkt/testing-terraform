module "lambda_function" {
  source = "git@github.com:terraform-aws-modules/terraform-aws-lambda.git?ref=v7.16.0"

  function_name = "test_lambda2"
  description   = "My awesome lambda function"
  handler       = "test_lambda.lambda_handler"
  runtime       = "python3.12"

  source_path = "../scripts/lambda/mylambda"

  tags = {
    Name = "my-lambda2"
  }
}