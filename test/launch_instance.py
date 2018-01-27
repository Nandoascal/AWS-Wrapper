import sys
import boto3


def main():

    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
                ImageId='ami-97785bed',
                MaxCount=1,
                MinCount=1)



if __name__ == '__main__':
    main()
