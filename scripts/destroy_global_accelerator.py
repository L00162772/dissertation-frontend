import os
import boto3

aws_region = os.environ['CHOOSEN_AWS_REGION']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
application_type = os.environ['APPLICATION_TYPE']

global_accelerator_region = "us-west-2"
base_application_dns = "atu-dissertation.com."

print("In destroy global accelerator")

client = boto3.client('globalaccelerator',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=global_accelerator_region)



list_accelerators_response = client.list_accelerators()
print(f"list_accelerators_response: {list_accelerators_response}")

distribution_id = ''
has_application_type_tag = False
accelerator_arn = ''
for accelerator in list_accelerators_response['Accelerators']:
    print(f" accelerator: {accelerator}")
    temp_accelerator_arn = accelerator['AcceleratorArn']
    print(f" temp_accelerator_arn: {temp_accelerator_arn}")

    tags_for_resource_response = client.list_tags_for_resource(ResourceArn=temp_accelerator_arn)
    print(f"tags_for_resource_response: {tags_for_resource_response}")

    has_application_type_tag = False
    for tag in tags_for_resource_response['Tags']:
        print(f"tag: {tag}")
        key = tag['Key']
        value = tag['Value']
        if key == 'Name' and value.lower() == application_type:
            has_application_type_tag = True
            accelerator_arn = temp_accelerator_arn

        print(f"has_application_type_tag: {has_application_type_tag}")

    if has_application_type_tag:
        disable_accelerator_response = client.update_accelerator( AcceleratorArn=accelerator_arn, Enabled=False)
        print(f"disable_accelerator_response: {disable_accelerator_response}")

        delete_accelerator_response = client.delete_accelerator(AcceleratorArn=accelerator_arn)
        print(f"delete_accelerator_response: {delete_accelerator_response}")

