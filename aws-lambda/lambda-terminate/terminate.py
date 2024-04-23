import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    ec2.instances.terminate()