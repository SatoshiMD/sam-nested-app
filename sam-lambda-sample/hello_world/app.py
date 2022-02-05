import json
import os
import boto3

# from my_layer import sample_summation


def lambda_handler(event, context):
    arr = [i for i in range(10)]
    # s = sample_summation(arr)

    return {
        "message": "hello world",
        # "sum": s
    }
