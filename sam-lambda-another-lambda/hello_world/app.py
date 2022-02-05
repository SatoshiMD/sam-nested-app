import json

import boto3


def lambda_handler(event, context):
    print(event)

    client = boto3.client('s3')

    return {
        "statusCode": 200,
        "body": {
            "message": "hello world",
            "event": event
        }
    }
