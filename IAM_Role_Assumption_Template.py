import boto3

def lambda_handler(event, context):
    # Initialize the STS client
    sts = boto3.client('sts')
    
    # Assume the specified IAM role
    assumed_role = sts.assume_role(
        RoleArn='arn:aws:iam::account-id:role/role-name',
        RoleSessionName='AssumeRoleSession'
    )
    
    # Extract temporary credentials
    credentials = assumed_role['Credentials']
    
    return {
        'statusCode': 200,
        'body': f"Role assumed. Access Key: {credentials['AccessKeyId']}"
    }
