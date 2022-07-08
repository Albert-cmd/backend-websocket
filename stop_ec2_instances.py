import sys
import boto3
from botocore.exceptions import ClientError
from flask_socketio import SocketIO, emit


def stop_instances():
    ec2 = boto3.client('ec2')
    try:
        ec2.stop_instances(InstanceIds=['i-06723d756cb3a859e', 'i-09862462e76bae184'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-06723d756cb3a859e', 'i-09862462e76bae184'], DryRun=False)
        print(response)
        response = ec2.describe_instance_status(InstanceIds=['i-06723d756cb3a859e', 'i-09862462e76bae184'],
                                                IncludeAllInstances=True)
        if response['InstanceStatuses'][0]['InstanceState']['Name'] == 'stopping':
            print(response)
            return True
    except ClientError as e:
        print(e)
        return False
