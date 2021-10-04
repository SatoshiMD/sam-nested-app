import boto3
import json

client = boto3.client('lambda')


def lambda_handler(event, context):
    try:
        print(event)

        path = event.get("pathParameters").get("proxy")
        params = path.split('/')
        lambda_name = params[0]

        params = {
            'FunctionName': lambda_name,
            'InvocationType': 'RequestResponse'
        }

        if event.get("httpMethod") != 'GET':
            params['Payload'] = event.get("body")

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
