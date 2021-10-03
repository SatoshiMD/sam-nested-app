import json


def lambda_handler(event, context):
    print(event)
    return json.dumps({
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"headerName": "headerValue"},
        "multiValueHeaders": {"headerName": ["headerValue", "headerValue2"]},
        "body": "..."
    })
