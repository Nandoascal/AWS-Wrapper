import sys
import boto3
from botocore.exceptions import ClientError


def turn_on_instance(instance_id, ec2):
    print('Turning on ' + instance_id + '...')

    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        #print(response)
    except ClientError as e:
        print(e)


def turn_off_instance(instance_id, ec2):
    print('Turning off ' + instance_id + '...')

    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        #print(response)
    except ClientError as e:
        print(e)


def reboot_instance(instance_id, ec2):
    print('Rebooting ' + instance_id + '...')

    try:
        response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
        #print(response)
    except ClientError as e:
        print(e)


def terminate_instance(instance_id, ec2):
    print('Terminating ' + instance_id + '...')

    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id], DryRun=False)
        #print(response)
    except ClientError as e:
        print(e)


def main():

    instance_id = sys.argv[2]
    action = sys.argv[1].upper()

    ec2 = boto3.client('ec2')

    if action == 'ON':
        turn_on_instance(instance_id, ec2)

    elif action == 'OFF':
        turn_off_instance(instance_id, ec2)

    elif action == 'REBOOT':
        reboot_instance(instance_id, ec2)

    elif action == 'TERMINATE':
        terminate_instance(instance_id, ec2)

    else:
        print('Action not recognized')

if __name__ == '__main__':
    main()
