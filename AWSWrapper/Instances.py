import boto3
from AWSWrapper.Instance import Instance


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instances:

    def __init__(self):
        self.instance_list = []
        self.add_existing_instances()


    def add_existing_instances(self):
        for instance in ec2_resource.instances.all():
            self.instance_list.append(Instance(instance.id))


    def get_all_instances(self):
        return self.instance_list


    def get_all_info(self):
        instances_info = {}

        for instance in self.instance_list:
            instances_info[instance.instance_id] = instance.get_info()
        return instances_info

    # Test that this actually works if you don't enter anything
    # Also add key pair creation
    def launch_instance(self, image_id, KeyPair=None, Name=None):

        if not Name:
            tag_specs = []
        else:
            tag_specs = [
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': Name
                            }
                        ]
                    }
                ]

        if not KeyPair:
            instance = ec2_resource.create_instances(
                    ImageId=image_id,
                    MaxCount=1,
                    MinCount=1,
                    TagSpecifications=tag_specs
                )
        else:
            instance = ec2_resource.create_instances(
                ImageId=image_id,
                MaxCount=1,
                MinCount=1,
                KeyName=KeyPair,
                TagSpecifications=tag_specs
            )
