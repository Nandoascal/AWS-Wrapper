import boto3


class Instances:

    def __init__(self):
        ec2 = boto3.resource('ec2', region_name='us-east-2')

        # gives back instance IDs and instance types of all instances.
        self.instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['*']}])

    def get_all_info(self):
        try:
            ec2info = dict()
            for instance in self.instances:
                ec2info[instance.id] = {
                    'ami_launch_index': instance.ami_launch_index,
                    'instance_type': instance.instance_type,
                    'state': instance.state['Name'],
                    'state_reason': instance.state_reason,
                    'state_transition_reason': instance.state_transition_reason,
                    'public_ip': instance.public_ip_address,
                    'private_ip': instance.private_ip_address,
                    'launch_time': instance.launch_time,
                    'kernel_id': instance.kernel_id,
                    'tags': instance.tags,
                    'architecture': instance.architecture,
                    'device_name': instance.block_device_mappings,
                    'client_token': instance.client_token,
                    'ebs_optimized': instance.ebs_optimized,
                    'elastic_gpu_associations': instance.elastic_gpu_associations,
                    'ena_support': instance.ena_support,
                    'hypervisor': instance.hypervisor,
                    'iam_instance_profile': instance.iam_instance_profile,
                    'image_id': instance.image_id,
                    'instance_id': instance.instance_id,
                    'key_name': instance.key_name,
                    'monitoring': instance.monitoring,
                    'network_interfaces_attribute': instance.network_interfaces_attribute,
                    'placement': instance.placement,
                    'platform': instance.platform,
                    'private_dns_name': instance.private_dns_name,
                    'product_codes': instance.product_codes,
                    'public_dns_name': instance.public_dns_name,
                    'ramdisk_id': instance.ramdisk_id,
                    'root_device_name': instance.root_device_name,
                    'root_device_type': instance.root_device_type,
                    'security_groups': instance.security_groups,
                    'source_dest_check': instance.source_dest_check,
                    'spot_instance_request_id': instance.spot_instance_request_id,
                    'sriov_net_support': instance.sriov_net_support,
                    'subnet_id': instance.subnet_id,
                    'virtualization_type': instance.virtualization_type,
                    'vpc_id': instance.vpc_id

                }
            return ec2info
        except:
            print('e')
