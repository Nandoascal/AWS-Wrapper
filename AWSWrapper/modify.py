import boto3

ec2 = boto3.client('ec2')


def mondify(instance, attribute, value):
    ec2.stop_instances(InstancesIds =[instance])
    waiter = ec2.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instance])

    ec2.modify_instance_attribute(InstanceId=instance, Attribute=attribute, Value=value)

    ec2.start_instances(InstancesIds=instance)
