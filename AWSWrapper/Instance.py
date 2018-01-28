import boto3
from botocore.exceptions import ClientError


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instance:


    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.instance = ec2_resource.Instance(self.instance_id)


    def get_info(self):
        info = {}

        try:
            info={
                'ami_launch_index': self.instance.ami_launch_index,
                'instance_type': self.instance.instance_type,
                'state': self.instance.state['Name'],
                'state_reason': self.instance.state_reason,
                'state_transition_reason': self.instance.state_transition_reason,
                'public_ip': self.instance.public_ip_address,
                'private_ip': self.instance.private_ip_address,
                'launch_time': self.instance.launch_time,
                'kernel_id': self.instance.kernel_id,
                'tags': self.instance.tags,
                'architecture': self.instance.architecture,
                'device_name': self.instance.block_device_mappings,
                'client_token': self.instance.client_token,
                'ebs_optimized': self.instance.ebs_optimized,
                'elastic_gpu_associations': self.instance.elastic_gpu_associations,
                'ena_support': self.instance.ena_support,
                'hypervisor': self.instance.hypervisor,
                'iam_instance_profile': self.instance.iam_instance_profile,
                'image_id': self.instance.image_id,
                'instance_id': self.instance.instance_id,
                'key_name': self.instance.key_name,
                'monitoring': self.instance.monitoring,
                'network_interfaces_attribute': self.instance.network_interfaces_attribute,
                'placement': self.instance.placement,
                'platform': self.instance.platform,
                'private_dns_name': self.instance.private_dns_name,
                'product_codes': self.instance.product_codes,
                'public_dns_name': self.instance.public_dns_name,
                'ramdisk_id': self.instance.ramdisk_id,
                'root_device_name': self.instance.root_device_name,
                'root_device_type': self.instance.root_device_type,
                'security_groups': self.instance.security_groups,
                'source_dest_check': self.instance.source_dest_check,
                'spot_instance_request_id': self.instance.spot_instance_request_id,
                'sriov_net_support': self.instance.sriov_net_support,
                'subnet_id': self.instance.subnet_id,
                'virtualization_type': self.instance.virtualization_type,
                'vpc_id': self.instance.vpc_id
            }
        except Exception as e:
            print(e)

        return info


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
