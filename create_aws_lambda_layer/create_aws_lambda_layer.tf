# Define provider and their configurations.
# Here, I am using shared AWS credentials.
provider "aws" {
  region = "ap-south-1"
}

# Creating AWS Lambda Layer for DynamoDB Database Operations
resource "aws_lambda_layer_version" "dynamoDBOperation" {
  filename = "../python.zip"
  layer_name = "dynamoDBOperation"

  compatible_runtimes = [
    "python3.8"
  ]
}