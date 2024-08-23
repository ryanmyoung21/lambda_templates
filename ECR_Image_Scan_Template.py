import boto3

def lambda_handler(event, context):
    # Initialize the ECR client
    ecr = boto3.client('ecr')
    
    # Define the repository name and image tag
    repository_name = 'your-repository'
    
    # Start an image scan for the specified image tag
    response = ecr.start_image_scan(
        repositoryName=repository_name,
        imageId={
            'imageTag': 'latest'
        }
    )
    
    return {
        'statusCode': 200,
        'body': f'Image scan initiated: {response["imageScanId"]}'
