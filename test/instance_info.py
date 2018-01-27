import sys
import boto3


def main():
    ec2 = boto3.resource('ec2')

    instance = ec2.Instance('i-06bb94ccddfcbdaa1')

    print('ami_launch_index: ', instance.ami_launch_index)
    print('architecture: ', instance.architecture)
    print('block_device_mappings: ', instance.block_device_mappings)
    print('client_token: ', instance.client_token)
    print('ebs_optimized: ', instance.ebs_optimized)
    print('elastic_gpu_associations: ', instance.elastic_gpu_associations)
    print('ena_support: ', instance.ena_support)
    print('hypervisor: ', instance.hypervisor)
    print('iam_instance_profile: ', instance.iam_instance_profile)
    print('image_id: ', instance.image_id)
    print('instance_id: ', instance.instance_id)
    print('instance_lifecycle: ', instance.instance_lifecycle)
    print('instance_type: ', instance.instance_type)
    print('kernel_id: ', instance.kernel_id)
    print('key_name:', instance.key_name)
    print('launch_time:', instance.launch_time)
    print('monitoring:', instance.monitoring)
    print('network_interfaces_attribute;', instance.network_interfaces_attribute)
    print('placement:', instance.placement)
    print('platform:', instance.platform)
    print('private_dns_name:', instance.private_dns_name)
    print('product_codes:', instance.product_codes)
    print('private_dns_name:', instance.public_dns_name)
    print('private_ip_address:', instance.private_ip_address)
    print('product_codes', instance.product_codes)
    print('public_dns_name:', instance.public_dns_name)
    print('public_ip_address:', instance.public_ip_address)
    print('ramdisk_id:', instance.ramdisk_id)
    print('root_device_name:', instance.root_device_name)
    print('root_device_type:', instance.root_device_type)
    print('security_groups:', instance.security_groups)
    print('source_dest_check:', instance.source_dest_check)
    print('spot_instance_request_id:', instance.spot_instance_request_id)
    print('sriov_net_support:', instance.sriov_net_support)
    print('state:', instance.state)
    print('state_reason:', instance.state_reason)
    print('state_transition_reason:', instance.state_transition_reason)
    print('subnet_id:', instance.subnet_id)
    print('tags:', instance.tags)
    print('virtualization_type:', instance.virtualization_type)
    print('vpc_id:', instance.vpc_id)


if __name__ == '__main__':
    main()
