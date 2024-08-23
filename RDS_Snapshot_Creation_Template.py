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
