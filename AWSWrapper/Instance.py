import boto3
from botocore.exceptions import ClientError


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


class Instance:


    def __init__(self, instance_id):
        self.instance_id = instance_id


    def get_info(self):
        info = {}

        try:
            info={
                'ami_launch_index': self.instance_id.ami_launch_index,
                'instance_type': self.instance_id.instance_type,
                'state': self.instance_id.state['Name'],
                'state_reason': self.instance_id.state_reason,
                'state_transition_reason': self.instance_id.state_transition_reason,
                'public_ip': self.instance_id.public_ip_address,
                'private_ip': self.instance_id.private_ip_address,
                'launch_time': self.instance_id.launch_time,
                'kernel_id': self.instance_id.kernel_id,
                'tags': self.instance_id.tags,
                'architecture': self.instance_id.architecture,
                'device_name': self.instance_id.block_device_mappings,
                'client_token': self.instance_id.client_token,
                'ebs_optimized': self.instance_id.ebs_optimized,
                'elastic_gpu_associations': self.instance_id.elastic_gpu_associations,
                'ena_support': self.instance_id.ena_support,
                'hypervisor': self.instance_id.hypervisor,
                'iam_instance_profile': self.instance_id.iam_instance_profile,
                'image_id': self.instance_id.image_id,
                'instance_id': self.instance_id.instance_id,
                'key_name': self.instance_id.key_name,
                'monitoring': self.instance_id.monitoring,
                'network_interfaces_attribute': self.instance_id.network_interfaces_attribute,
                'placement': self.instance_id.placement,
                'platform': self.instance_id.platform,
                'private_dns_name': self.instance_id.private_dns_name,
                'product_codes': self.instance_id.product_codes,
                'public_dns_name': self.instance_id.public_dns_name,
                'ramdisk_id': self.instance_id.ramdisk_id,
                'root_device_name': self.instance_id.root_device_name,
                'root_device_type': self.instance_id.root_device_type,
                'security_groups': self.instance_id.security_groups,
                'source_dest_check': self.instance_id.source_dest_check,
                'spot_instance_request_id': self.instance_id.spot_instance_request_id,
                'sriov_net_support': self.instance_id.sriov_net_support,
                'subnet_id': self.instance_id.subnet_id,
                'virtualization_type': self.instance_id.virtualization_type,
                'vpc_id': self.instance_id.vpc_id
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
