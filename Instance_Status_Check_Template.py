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
