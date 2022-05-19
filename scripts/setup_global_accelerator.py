import os
import boto3

aws_region = os.environ['CHOOSEN_AWS_REGION']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
hosted_zone_id = os.environ['HOSTED_ZONE_ID']

print("aws_region:", aws_region)
print("aws_access_key_id:", aws_access_key_id)
print("aws_secret_access_key:", aws_secret_access_key)
print("In invalidate_cloudfront_distribution")

client = boto3.client('globalaccelerator',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)

route53_client = boto3.client('route53',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)
    
print("Here 2")  
list_accelerators_response = client.list_accelerators()
print(f"list_accelerators_response: {list_accelerators_response}")

distribution_id = ''
for accelerator in list_accelerators_response['Accelerators']:
    print(f" accelerator: {accelerator}")
    accelerator_arn = accelerator['AcceleratorArn']
    print(f" accelerator_arn: {accelerator_arn}")

    tags_for_resource_response = client.list_tags_for_resource(Resource=accelerator_arn)
    print(f"tags_for_resource_response: {tags_for_resource_response}")

    has_frontend_tag = False
    for tag in tags_for_resource_response['Tags']['Items']:
        print(f" tag: {tag}")
        key = tag['Key']
        value = tag['Value']
        if key == 'Name' and value.lower() == 'frontend':
            has_frontend_tag = True
        
        print(f" has_frontend_tag: {has_frontend_tag}")

    
    if has_frontend_tag:
        break;
    else:
        create_accelerator_response = client.create_accelerator(
            Name='frontend',
            IpAddressType='IPV4',
            Enabled=True,
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'frontend'
                },
            ]
        )
        print(f"create_accelerator_response: {create_accelerator_response}")

        change_resource_record_sets_response = route53_client.change_resource_record_sets(
                        HostedZoneId=hosted_zone_id,
                        ChangeBatch={
                            'Changes': [
                                    'Action': 'CREATE',
                                    'ResourceRecordSet': {
                                        'Name': 'frontend',
                                        'Type': 'A',
                                        'SetIdentifier': 'string',
                                        'Region': 'us-east-1',
                                        'TTL': 60,
                                        'AliasTarget': {
                                            'HostedZoneId': hosted_zone_id,
                                            'DNSName': 'string',
                                            'EvaluateTargetHealth': True
                                        }
                                    }
                                
                            ]
                        }
                    )
        print(f"change_resource_record_sets_response: {create_accelerator_response}")