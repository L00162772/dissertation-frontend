import boto3
print("In invalidate_cloudfront_distribution")

client = boto3.client('cloudfront')
response = client.list_distributions()
print(f"response: {response}")