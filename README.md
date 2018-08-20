# python-hello

To run:

    docker run --rm -v "$PWD":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler '{ "name": "world" }'
