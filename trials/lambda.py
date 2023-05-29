import json
import boto3

ENDPOINT_NAME = 'sagemaker-xgboost-2023-04-23-20-02-45-272'
runtime = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    inputs = event['data']
    result = []
    for input in inputs:
        serialized_input = ','.join(map(str, input))

        reponse = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                          ContentType='text/csv',
                                          Body=serialized_input)
        result.append(reponse['Body'].read().decode('utf-8'))
    return result
