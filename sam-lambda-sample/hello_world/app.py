import json
import os
import boto3

from my_layer import sample_summation


def lambda_handler(event, context):
    bucket = os.getenv('SamplebucketName')
    print(bucket)

    client = boto3.client('s3')
    response = client.list_objects(
        Bucket=bucket
    )
    print(response)

    arr = [i for i in range(10)]
    s = sample_summation(arr)

    return {
        "body": {
            "message": "hello world",
            "sum": s
        }
    }
