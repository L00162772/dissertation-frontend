import os
import boto3

aws_region = os.environ['CHOOSEN_AWS_REGION']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

print("aws_region:", aws_region)
print("aws_access_key_id:", aws_access_key_id)
print("aws_secret_access_key:", aws_secret_access_key)
print("In invalidate_cloudfront_distribution")

client = boto3.client('cloudfront', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)
print("Here 2")  
list_distributions_response = client.list_distributions()
print(f"list_distributions_response: {list_distributions_response}")