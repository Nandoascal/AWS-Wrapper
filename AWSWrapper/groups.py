import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')


def make_group(name, description, ip_permissions):
    try:
        response = ec2.create_security_group(GroupName=name, Description=description, VpcId=vpc_id)

        security_group_id = response['GroupId']
        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=ip_permissions)

    except ClientError as e:
        print(e)


def delete_group(GroupId):
    try:
        response = ec2.delete_security_group(GroupId=GroupId)
    except ClientError as e:
        print(e)
