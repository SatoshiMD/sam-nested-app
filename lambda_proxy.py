import boto3
import json

client = boto3.client('lambda')


def lambda_handler(event, context):
    try:
        print(event)

        lambda_name = event.get("pathParameters").get("service")
        url_params = event.get("pathParameters").get("params")

        params = {
            'FunctionName': lambda_name,
            'InvocationType': 'RequestResponse'
        }

        if event.get("httpMethod") != 'GET':
            params['Payload'] = {
                "parameters": url_params,
                "body": event.get("body")
            }

        response = client.invoke(**params)
        data = response['Payload'].read().decode('utf8').replace('"', '\"')

        print(json.loads(data))
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": data
        }
    except Exception as e:
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": str(e)
        }
