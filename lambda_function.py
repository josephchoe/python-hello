from __future__ import print_function

def lambda_handler(event, context):
  return "Hello, " + event['name'] + "!"  # Echo back the first key value
