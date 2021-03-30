# Sample Code for Chalice projects

I have created two Chalice projects (AWS Lambda Functions) and written a script which is common for both AWS Lambda Functions.


### AWS Lambda Functions:
- `students_service` - Chalice Project
- `teachers_service` - Chalice Project

### AWS Lambda Layers:
- `python` - Simple script need to convert it into .zip file to deploy as Lambda Layer


`utilities` is just a package to create tables in AWS DynamoDB and defined schemas for tables.
1.  First, you need to create database tables in AWS DynamoDB. So, use `utilities` package and run `create_tables.py` module to create tables.
2.  Create a layer - create .zip file of directory `python` given in project and upload it into AWS Lambda Layers.
    You can use `terraform` script to deploy AWS Lambda Layer. The script written for that is `create_aws_lambda_layer/create_aws_lambda_layer.tf` - [steps to apply terraform script](https://github.com/Evergreenies/terraform_scripts/blob/main/README.md)
3.  Now, copy ARN of the layer and update/add `layers` keys in `<project-name>/.chalice/config.json` like -
```json
{
  "version": "2.0",
  "layers": [
    "<ARN>"
  ],
  "app_name": "teachers_service",
  "stages": {
    "dev": {
      "api_gateway_stage": "api"
    }
  }
}
```
4.  Deploy changes on AWS Lambda by below command.

After this command you will receive a URL provided by AWS API Gateway. You can use that URL to test endpoints.
```shell
(venv)$ chalice deploy
```

Now, test endpoints -
```shell
$ # Get all students data
$ curl --location --request GET 'https://<URL>/all-students'
$
$ # Get specific student data
$ curl --location --request GET 'https://<URL>/student' \
--header 'Content-Type: application/json' \
--data-raw '{
    "s_id": 1, 
    "username": "suyogshimpi"
}'
$
$ # Same for teachers as well
```

### General steps to create Chalice project and deploy them:
1.  Create virtual environment and install requirements -
```shell
pip install -r requirements.txt
```

2.  Create Chalice project -
```shell
(venv)$ chalice new-project <project-name>
```

3.  To test project on local -
```shell
(venv)$ chalice local
```

4.  To deploy project on AWS -
```shell
(venv)$ chalice deploy
```
