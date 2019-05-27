import json

def lambda_handler(event, context):
    # TODO implement
    print(str(event))
    print(str(context))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
