import boto3

def lambda_handler(event, context):
    # Initialize the S3 client
    s3 = boto3.client('s3')
    
    # Specify the bucket name
    bucket_name = 'your-bucket-name'
    
    # Define the lifecycle policy to delete objects older than 30 days
    lifecycle_policy = {
        'Rules': [
            {
                'ID': 'Delete old objects',
                'Prefix': '',
                'Status': 'Enabled',
                'Expiration': {
                    'Days': 30
                }
            }
        ]
    }
    
    # Apply the lifecycle policy to the specified S3 bucket
    s3.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_policy
    )
    
    return {
        'statusCode': 200,
        'body': 'Lifecycle policy applied to S3 bucket'
    }
