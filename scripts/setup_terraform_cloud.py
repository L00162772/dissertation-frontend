import os
import requests

aws_region = os.environ['CHOOSEN_AWS_REGION']
tf_api_token = os.environ['TF_API_TOKEN']

print("aws_region:", aws_region)
print("tf_api_token:", tf_api_token)

base_url = "https://app.terraform.io/api/v2"
workspace_name = f"frontend-{aws_region}"
organization_name = "dissertation"

get_workspaces_url = f"{base_url}/organizations/{organization_name}/workspaces/{workspace_name}"
print(f"get_workspaces_url:{get_workspaces_url}")

get_workspaces_response=requests.get("http://www.example.com/", headers={"Authorization": f"Bearer {tf_api_token}"})
print(f"get_workspaces_response:{get_workspaces_response}")

# CHOOSEN_AWS_REGION=us-east-1 TF_API_TOKEN=7B1IyXaHshr7Kg.atlasv1.weHEIKHzHQUIVBHSDHrXr1ylqO2Ua4Qp8VyxNMNnd9nKpW53Ms3euN8yUNmBCi4GRE0 python3 scripts/setup_terraform_cloud.py