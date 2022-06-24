# dissertation-frontend
Frontend Repository for the Dissertation practical
 
## Folder Structure
terraform: Infrastructure as Code (IaC)
frontend: React frontend code
 
## Terraform Instructions
### Prequisite Software:
Terraform: https://www.terraform.io/

### Run terraform code
For best results - it is recommended to follow the deployment process outlined in the Wiki https://github.com/L00162772/dissertation-frontend/wiki/Deployment-Process for testing the code. Running terraform locally will required that some variables and attributes are tweaked. The code that is checked in has been tested using the deployment process and terraform cloud.

#### Execute plan
```
cd terraform
terraform init
terraform plan
```

#### Create Infrastructure
```
cd terraform
terraform apply --auto-approve
```

#### Destroy Infrastructure
```
cd terraform
terraform destroy --auto-approve
```


### Run frontend project - Note: Backend project needs to already be running on AWS
```
cd frontend
npm install
npm start
```### ToDO
Automate certificate approval after it is created
