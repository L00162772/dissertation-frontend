# dissertation-frontend
Frontend Repository for the Dissertation
See: https://andyjones.co/articles/react-aws-terraform-github-actions/


## Folder Structure
terraform: Infrastructure as Code (IaC)
frontend: React frontend code

## Terraform Instructions
### Prequisite Software:
Terraform: https://www.terraform.io/

### Run terraform code
#### Execute plan
cd terraform
terraform init
terraform plan

#### Create Infrastructure
cd terraform
terraform apply --auto-approve

#### Destroy Infrastructure
cd terraform
terraform destroy --auto-approve


## Frontend Instructions
### Prequisite Software:
NodeJs: https://nodejs.org/en/

### Run frontend project
cd frontend
npm install
npm start

### ToDO
Automate certificate approval after it is created