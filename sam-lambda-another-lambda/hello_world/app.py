import json
import boto3
import os


def lambda_handler(event, context):
    bucket = os.getenv('SamplebucketName')
    print(bucket)

    # client = boto3.client('s3')
    # response = client.list_objects(
    #     Bucket=bucket
    # )
    # print(response)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
