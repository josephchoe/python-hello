# python-hello

To install:

    pip install -t . -r requirements.txt 

To run:

    docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler '{ "name": "world" }'

AWS API Gateway

    https://cqwybngfb0.execute-api.us-east-1.amazonaws.com/production/helloWorld?name=Test
