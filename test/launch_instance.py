import sys
import boto3


def main():

    name = sys.argv[1]

    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
                ImageId='ami-97785bed',
                MaxCount=1,
                MinCount=1,
                TagSpecifications=[
                    {
                        'ResourceType':'instance',
                        'Tags':[
                                {
                                'Key':'Name',
                                'Value':name
                                }
                            ]
                        }
                    ])


if __name__ == '__main__':
    main()
