import os
import boto3

aws_region = os.environ['CHOOSEN_AWS_REGION']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

accelerator_region = "us-west-2"
base_region = "us-east-1"
base_dns = "atu-dissertation.com."

print("aws_region:", aws_region)
print("aws_access_key_id:", aws_access_key_id)
print("aws_secret_access_key:", aws_secret_access_key)
print("In setup global accelerator")

client = boto3.client('globalaccelerator',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=accelerator_region)

route53_client = boto3.client('route53',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              region_name=base_region)

print("Here 2")
list_accelerators_response = client.list_accelerators()
print(f"list_accelerators_response: {list_accelerators_response}")

distribution_id = ''
has_frontend_tag = False
accelerator_arn = ''
for accelerator in list_accelerators_response['Accelerators']:
    print(f" accelerator: {accelerator}")
    accelerator_arn = accelerator['AcceleratorArn']
    print(f" accelerator_arn: {accelerator_arn}")

    tags_for_resource_response = client.list_tags_for_resource(
        ResourceArn=accelerator_arn)
    print(f"tags_for_resource_response: {tags_for_resource_response}")

    has_frontend_tag = False
    for tag in tags_for_resource_response['Tags']:
        print(f" tag: {tag}")
        key = tag['Key']
        value = tag['Value']
        if key == 'Name' and value.lower() == 'frontend':
            has_frontend_tag = True

        print(f" has_frontend_tag: {has_frontend_tag}")

    if has_frontend_tag:
        break

if not has_frontend_tag:
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

    hosted_zones_response = route53_client.list_hosted_zones()
    print(f"hosted_zones_response: {hosted_zones_response}")
    hosted_zone_id = ''
    for hosted_zone in hosted_zones_response['HostedZones']:
        print(f"hosted_zone: {hosted_zone}")
        if hosted_zone['Name'].lower() == base_dns:
            hosted_zone_id = hosted_zone['Id']
            break

    print(f"hosted_zone_id 1:{hosted_zone_id}")
    str = '/hostedzone/'
    hosted_zone_id = hosted_zone_id[len(str):]
    print(f"hosted_zone_id 2:{hosted_zone_id}")
    change_resource_record_sets_response = route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
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
                },
            ]
        }
    )
    print(
        f"change_resource_record_sets_response: {create_accelerator_response}")


create_listener_response = client.create_listener(
    AcceleratorArn=accelerator_arn,
    PortRanges=[
        {
            'FromPort': 80,
            'ToPort': 80
        },
    ],
    Protocol='TCP',
    ClientAffinity='NONE'
)
print(f"create_listener_response:{create_listener_response}")

create_endpoint_group_response = client.create_endpoint_group(
    ListenerArn=create_listener_response['Listener']['ListenerArn'],
    EndpointGroupRegion=aws_region,
    EndpointConfigurations=[
        {
            'EndpointId': aws_region,
            'Weight': 123,
            'ClientIPPreservationEnabled': False
        },
    ],
    HealthCheckPort=80,
    HealthCheckProtocol='HTTP',
    HealthCheckPath='/index.html',
    HealthCheckIntervalSeconds=30,
    ThresholdCount=3,
    IdempotencyToken='string',
    PortOverrides=[
        {
            'ListenerPort': 80,
            'EndpointPort': 80
        },
    ]
)
print(f"create_endpoint_group_response:{create_endpoint_group_response}")
