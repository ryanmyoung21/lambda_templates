import boto3

def lambda_handler(event, context):
    # Initialize the SNS client
    sns = boto3.client('sns')
    
    # Extract the message from the incoming SNS event
    message = event['Records'][0]['Sns']['Message']
    
    # Publish the message to another SNS topic
    response = sns.publish(
        TopicArn='arn:aws:sns:region:account-id:another-topic',
        Message=message
    )
    
    return {
        'statusCode': 200,
        'body': 'Message forwarded successfully'
    }
