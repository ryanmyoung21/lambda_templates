import json
import boto3

def lambda_handler(event, context):
    # Initialize the SNS client
    client = boto3.client('sns')
    
    # Create a message with the auto-scaling event details
    message = f"Auto-scaling event detected: {json.dumps(event)}"
    
    # Publish the message to the specified SNS topic
    response = client.publish(
        TopicArn='arn:aws:sns:region:account-id:your-topic',
        Message=message,
        Subject='Auto-Scaling Notification'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully')
    }
