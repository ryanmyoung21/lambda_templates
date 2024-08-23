import boto3

def lambda_handler(event, context):
    # Initialize the CloudFormation client
    cf = boto3.client('cloudformation')
    
    # Define stack name and template URL
    stack_name = 'your-stack-name'
    template_url = 'https://s3.amazonaws.com/your-bucket/your-template.yaml'
    
    # Create the CloudFormation stack with the provided template
    response = cf.create_stack(
        StackName=stack_name,
        TemplateURL=template_url,
        Capabilities=['CAPABILITY_IAM']
    )
    
    return {
        'statusCode': 200,
        'body': f'Stack creation initiated: {response["StackId"]}'
    }
