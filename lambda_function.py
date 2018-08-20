import json

def lambda_handler(event, context):
  message = hello(event['name'])
  body = {
    "message": message
  }

  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }

  return response

def hello(name):
  return "Hello, %s!" % name
