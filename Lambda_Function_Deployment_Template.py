import boto3

def lambda_handler(event, context):
    # Initialize the Lambda client
    lambda_client = boto3.client('lambda')
    
    # Define the Lambda function name and S3 bucket details
    function_name = 'your-lambda-function'
    
    # Update the Lambda function code from the S3 bucket
    response = lambda_client.update_function_code(
        FunctionName=function_name,
        S3Bucket='your-bucket',
        S3Key='path/to/your/code.zip'
    )
    
    return {
        'statusCode': 200,
        'body': f'Lambda function updated: {response["FunctionArn"]}'
    }
