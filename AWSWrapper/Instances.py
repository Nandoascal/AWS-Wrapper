import boto3


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instances:

    def __init__(self):
        self.instance_list = []


    def get_all_info(self):
        instances_info = {}

        for instance in self.instance_list:
            instances_info[instance.instance_id] = instance.get_info()

    ### Add key pair functionality to both ###
    def launch_named_instance(self, name, image_id):
        instance = ec2_resource.create_instances(
                ImageId=image_id,
                MaxCount=1,
                MinCount=1,
                TagSpecifications=[
                    {
                        'ResourceType':'instance',
                        'Tags':[
                            'Key':'Name',
                            'Value':name
                            ]
                        }
                    ]
                )


    def launch_instance(self, image_id):
        instance = ec2_resource.create_instances(
                ImageId=image_id,
                MaxCount=1,
                MinCount=1
                )
