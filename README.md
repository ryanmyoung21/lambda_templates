This repository contains a set of AWS Lambda function templates tailored for DevOps engineers. These templates can help automate various tasks such as auto-scaling notifications, EC2 instance status checks, S3 bucket lifecycle management, and more.

Table of Contents

Introduction
Templates
1. Auto-scaling Notification
2. EC2 Instance Status Check
3. S3 Bucket Lifecycle Policy
4. CloudFormation Stack Deployment
5. RDS Snapshot Creation
6. SNS Message Forwarding
7. IAM Role Assumption
8. Lambda Function Deployment
9. CloudWatch Alarm Creation
10. ECR Image Scan
Setup Instructions
Contributing

Introduction
This collection of AWS Lambda functions is designed to assist DevOps engineers in automating common tasks. Each function is tailored to interact with various AWS services like EC2, S3, RDS, CloudFormation, and more.

Templates
1. Auto-scaling Notification
This Lambda function sends an SNS notification when an auto-scaling event is detected.

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

2. EC2 Instance Status Check
This Lambda function checks the status of EC2 instances and logs their state.


import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')
    
    # Retrieve the status of all EC2 instances
    response = ec2.describe_instances()
    
    # Iterate through the instances and log their state
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    
    return {
        'statusCode': 200,
        'body': 'EC2 instance status checked'
    }

3. S3 Bucket Lifecycle Policy
This function applies a lifecycle policy to an S3 bucket to delete objects older than 30 days.


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

4. CloudFormation Stack Deployment
This Lambda function initiates the creation of a CloudFormation stack using a specified template.


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

5. RDS Snapshot Creation
This function creates a snapshot of an RDS instance.


import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize the RDS client
    rds = boto3.client('rds')
    
    # Define the RDS instance identifier and snapshot ID
    db_instance_identifier = 'your-db-instance-id'
    snapshot_id = f"{db_instance_identifier}-snapshot-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    
    # Create a snapshot of the RDS instance
    response = rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceIdentifier=db_instance_identifier
    )
    
    return {
        'statusCode': 200,
        'body': f'DB snapshot creation initiated: {response["DBSnapshot"]["DBSnapshotIdentifier"]}'
    }

6. SNS Message Forwarding
Forwards an SNS message from one topic to another.


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

7. IAM Role Assumption
Assumes an IAM role and returns temporary credentials.


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

8. Lambda Function Deployment
Deploys a new version of a Lambda function from a specified S3 bucket.


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

9. CloudWatch Alarm Creation
Creates a CloudWatch alarm to monitor high CPU utilization.


import boto3

def lambda_handler(event, context):
    # Initialize the CloudWatch client
    cloudwatch = boto3.client('cloudwatch')
    
    # Create a CloudWatch alarm for CPU utilization
    response = cloudwatch.put_metric_alarm(
        AlarmName='HighCPUUtilization',
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Statistic='Average',
        Period=300,
        Threshold=80.0,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        AlarmActions=['arn:aws:sns:region:account-id:your-topic']
    )
    
    return {
        'statusCode': 200,
        'body': 'CloudWatch alarm created successfully'
    }

10. ECR Image Scan
Starts a scan of an image in an ECR repository.


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
    }


Setup Instructions

Create an AWS Lambda Function:

Go to the AWS Lambda console.
Click on "Create function".
Choose "Author from scratch".
Configure basic settings and paste the desired Lambda function code.

Set Permissions:

Ensure your Lambda function has the necessary IAM role and permissions to interact with AWS services such as EC2, S3, CloudFormation, etc. You may need to attach IAM policies to the Lambda execution role to grant appropriate access.

Configure Triggers:

Set up triggers for your Lambda functions according to your needs. For example, you can configure CloudWatch Events for scheduled tasks, S3 bucket events for object changes, or SNS topics for notifications.

Test the Function:

Use the "Test" feature in the Lambda console to simulate the function execution and verify that it behaves as expected. You can provide sample event data to test different scenarios.
Contributing

Feel free to submit issues, improvements, or additional templates via pull requests. Please ensure to follow the project's coding standards and include documentation for any new functionality. Contributions are welcome to enhance the automation and functionality provided by these Lambda functions.


This README provides a detailed overview of each Lambda function template and instructions for setup, permissions, and testing. If you have any further questions or need additional assistance, feel free to ask!
