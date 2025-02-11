import json
import boto3
print(boto3.__version__)

def lambda_handler(event, context):
  return{
    'statusCode':200,
    'body':json.dumps('Hello from Lambda!')
  }
