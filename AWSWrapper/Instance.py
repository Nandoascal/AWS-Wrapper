import boto3
from botocore.exceptions import ClientError


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instance:


    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.instance = ec2_resource.Instance(self.instance_id)


    def get_info(self):

        info = ec2_client.describe_instances(InstanceIds=[self.instance_id])

        return info['Reservations'][0]['Instances']


    def modify(self, attribute, value):
        ec2_client.stop_instances(InstanceIds=[self.instance_id])

        waiter= ec2_client.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[self.instance_id])

        ec2_client.modify_instance_attribute(InstanceId=self.instance_id,
                Attribute=attribute,
                Value=value)

        ec2_client.start_instances(InstanceIds=[self.instance_id])

    def add_tag(self, instanceId):
        response = ec2_client.create_tags(
        Resources=[
            instanceId,
        ],
        Tags=[
            {
                'Key': 'testTag',
                'Value': 'Jack is a shit'
            },
        ]
    )

    def delete_tags(self, instanceId, key, value):
        response = ec2_client.delete_tags(
            Resources=[
                instanceId,
            ],
            Tags=[
                {
                    'Key': key,
                    'Value': value,
                },
            ],
        )

    def change_tags(self, instanceId, Key, Value, newKey, newValue):
        response = ec2_client.delete_tags(
            Resources=[
                instanceId,
            ],
            Tags=[
                {
                    'Key': Key,
                    'Value': Value,
                },
            ],
        )

        response = ec2_client.create_tags(
            Resources=[
                'i-085415335fc9aa3ae'
            ],
            Tags=[
                {
                    'Key': newKey,
                    'Value': newValue,
                },
            ],
        )

    def turn_on(self):
        try:
            response = ec2_client.start_instances(InstanceIds=[self.instance_id],
                    DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                print('Your permissions are wrong')
                raise
        try:
            response = ec2_client.start_instances(InstanceIds=[self.instance_id],
                    DryRun=False)
        except ClientError as e:
            print(e)


    def turn_off(self):
        try:
            response = ec2_client.stop_instances(InstanceIds=[self.instance_id],
                    DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                print('Your permissions are fucked')
                raise
        try:
            response = ec2_client.stop_instances(InstanceIds=[self.instance_id],
                    DryRun=False)
        except ClientError as e:
            print(e)


    def reboot(self):
        try:
            response = ec2_client.reboot_instances(InstanceIds=[self.instance_id],
                    DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                print('Your permissions are fucked')
                raise
        try:
            response = ec2_client.reboot_instances(InstanceIds=[self.instance_id],
                    DryRun=False)
        except ClientError as e:
            print(e)


    def terminate(self):
        try:
            response = ec2_client.reboot_instances(InstanceIds=[self.instance_id],
                    DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                print('Your permissions are fucked')
                raise
        try:
            response = ec2_client.reboot_instances(InstanceIds=[self.instance_id],
                    DryRun=False)
        except ClientError as e:
            print(e)
