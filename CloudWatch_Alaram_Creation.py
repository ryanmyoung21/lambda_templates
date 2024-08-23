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
