import boto3
import sys


def describe(ec2):
    response = ec2.describe_key_pairs()
    print(response)


def create(name, ec2):
    print('Creating key pair named ' + name + '...')

    response = ec2.create_key_pair(KeyName=name)
    print(response)


def delete(name, ec2):
    print('Deleting key pair named ' + name + '...')

    response = ec2.delete_key_pair(KeyName=name)
    print(response)


def main():

    ec2 = boto3.client('ec2')
    action = sys.argv[1].upper()

    if action == 'SHOW':
        describe(ec2)
    elif action == 'CREATE':
        name = sys.argv[2]
        create(name, ec2)
    elif action == 'DELETE':
        name = sys.argv[2]
        delete(name, ec2)
    else:
        print('Action not recognized, exiting')


if __name__ == '__main__':
    main()
