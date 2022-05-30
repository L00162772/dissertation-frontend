import os
import boto3

aws_region = os.environ['CHOOSEN_AWS_REGION']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
start_synthetic_monitor = os.environ['START_SYNTHETIC_MONITOR']


print("In configure Synthetic Monitor")

client = boto3.client('synthetics',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=aws_region)


synthetic_monitor_name = 'frontend_canary'
print(f"start_synthetic_monitor:{start_synthetic_monitor}")
if start_synthetic_monitor.lower() == "true":
    print("Starting the synthetic monitor")
    start_canary_response = client.start_canary(Name=synthetic_monitor_name)

    print(f"start_canary_response:{start_canary_response}")
else:
    print("Stopping the synthetic monitor")
    stop_canary_response = client.stop_canary(Name=synthetic_monitor_name)

    print(f"stop_canary_response:{stop_canary_response}")