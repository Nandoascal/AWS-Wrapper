import boto3
from botocore.exceptions import ClientError

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instance:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.instance = ec2_resource.Instance(self.instance_id)

    def get_info(self):
        """
        obtains all attribute information for the instance.
        """

        info = ec2_client.describe_instances(InstanceIds=[self.instance_id])

        return info['Reservations'][0]['Instances']

    def modify(self, attribute, value):
        """
        modifies an attribute of the instance
        :param attribute: the field to be changed
        :param value: the new value you wish ti input
        """
        ec2_client.stop_instances(InstanceIds=[self.instance_id])

        waiter = ec2_client.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[self.instance_id])

        ec2_client.modify_instance_attribute(InstanceId=self.instance_id,
                                             Attribute=attribute,
                                             Value=value)

        ec2_client.start_instances(InstanceIds=[self.instance_id])

    def add_tag(self, key, value):
        """
        adds a tag to an instance
        """
        response = ec2_client.create_tags(
            Resources=[
                self.instance_id,
            ],
            Tags=[
                {
                    'Key': key,
                    'Value': value
                },
            ]
        )

    def delete_tag(self, key, value):
        """
        boto3 is junk and requires you to input all the information of a tag to delete it.
        :param key: the tag name
        :param value: the description of the tag
        """
        response = ec2_client.delete_tags(
            Resources=[
                self.instance_id,
            ],
            Tags=[
                {
                    'Key': key,
                    'Value': value,
                },
            ],
        )

    def change_tag(self, Key, Value, newKey, newValue):
        """
        boto3 has no real way of editing the keyname or valuename as far as I could tell
        so my best solution was to delete the tag and remake it.
        :param Key: original name/key of tag
        :param Value: original description/value of the tag
        :param newKey: new name/key
        :param newValue: new description/value
        """

        self.delete_tag(Key, Value)

        self.add_tag(newKey, newValue)


    def turn_on(self):
        """
        turns on a stopped instance
        """
        try: # Tests your permissions before actually going through with it
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
        """
        turns off a running instance
        :return:
        """
        try: # Tests your permissions before actually going through with it
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
        """
        reboots an instance
        """
        try: # Tests your permissons before actually going through with it
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
        """
        deletes the instance
        """
        try: # Tests your permissions before actually going through with it
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
