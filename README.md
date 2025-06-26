# AWS Todo App Auto Scaling Infrastructure

This repository contains Terraform code to deploy a highly available Todo application on AWS with auto scaling capabilities.

## Architecture

- **VPC**: Custom VPC with public and private subnets across multiple AZs
- **EC2**: Auto Scaling Group with Launch Template running Node.js Todo app
- **Load Balancer**: Application Load Balancer for traffic distribution
- **Database**: RDS MySQL Multi-AZ for high availability
- **Monitoring**: CloudWatch for metrics, alarms, and dashboards
- **Security**: Security Groups with least privilege access

## Features

### Todo Application

- ✅ Create, read, update, delete todos
- ✅ Mark todos as complete/incomplete
- ✅ Real-time instance information display
- ✅ Responsive design for mobile and desktop
- ✅ Load testing functionality
- ✅ Statistics dashboard

### Infrastructure

- ✅ Auto scaling based on CPU utilization
- ✅ Multi-AZ deployment for high availability
- ✅ Load balancing across instances
- ✅ Database backups and Multi-AZ
- ✅ CloudWatch monitoring and alarms
- ✅ Infrastructure as Code with Terraform

## Prerequisites

1. **AWS CLI** configured with appropriate credentials
2. **Terraform** v1.0 or later
3. **AWS Account** with sufficient permissions

## Deployment Instructions

### 1. Clone and Navigate

```bash
cd "C:\Users\Reji\Pictures\terraform\3. Auto Scaling Web Application"
```

### 2. Create SSH Key Pair

Create an AWS Key Pair for SSH access to EC2 instances:

```bash
# Using AWS CLI
aws ec2 create-key-pair --key-name todo-app-key --query 'KeyMaterial' --output text > todo-app-key.pem

# Set proper permissions (Linux/Mac)
chmod 400 todo-app-key.pem

# For Windows PowerShell
icacls todo-app-key.pem /inheritance:r /grant:r "$env:USERNAME:R"
```

Or create it through AWS Console:

1. Go to EC2 → Key Pairs
2. Create new key pair named `todo-app-key`
3. Download the `.pem` file

### 3. Configure Variables

Copy the example variables file and customize:

```bash
Copy-Item terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars` and update these important values:

```hcl
aws_region = "us-east-1"
project_name = "todo-app"
key_pair_name = "todo-app-key"  # Name of your SSH key pair
db_username = "dbadmin"
db_password = "YourVerySecurePassword123!"  # Change this!
```

### 3. Initialize Terraform

```bash
terraform init
```

### 4. Plan Deployment

```bash
terraform plan
```

### 5. Deploy Infrastructure

```bash
terraform apply
```

Type `yes` when prompted to confirm.

### 6. Access Your Application

After deployment completes (5-10 minutes), you'll see outputs including:

- `load_balancer_url`: Your Todo app URL
- `cloudwatch_dashboard_url`: Monitoring dashboard

## Application Usage

### Todo App Features

1. **Add Todos**: Use the form to create new todos with title and description
2. **Complete Todos**: Click the circle button to mark as complete
3. **Delete Todos**: Click the trash button to remove todos
4. **View Stats**: See total, pending, and completed todo counts
5. **Instance Info**: View which EC2 instance served your request

### Load Testing

The app includes a built-in load test feature that will trigger auto scaling:

1. Click "Load Test" button
2. Monitor the requests hitting different instances
3. Watch CloudWatch metrics for scaling events

### SSH Access to Instances

You can SSH into the EC2 instances for debugging or manual configuration:

```bash
# Get instance IP from AWS Console or Terraform output
ssh -i todo-app-key.pem ec2-user@<INSTANCE-PRIVATE-IP>

# Or use Session Manager (no SSH key required)
aws ssm start-session --target <INSTANCE-ID>
```

**Note**: Instances are in private subnets, so you'll need to:

1. Use a bastion host in public subnet, OR
2. Use AWS Session Manager (recommended), OR
3. Connect via VPN/Direct Connect

**Quick Session Manager Setup:**

```bash
# Install Session Manager plugin
# Then connect without SSH keys:
aws ssm start-session --target i-1234567890abcdef0
```

## Monitoring

### CloudWatch Dashboard

Access the automatically created dashboard via the output URL to monitor:

- CPU utilization across instances
- Auto Scaling Group metrics
- Load Balancer performance
- Request counts and response times

### Auto Scaling Triggers

- **Scale Up**: When CPU > 70% for 10 minutes
- **Scale Down**: When CPU < 20% for 10 minutes
- **Min Instances**: 2
- **Max Instances**: 6

## File Structure

```
├── main.tf                 # Main configuration entry point
├── provider.tf            # AWS provider configuration
├── variables.tf           # Input variables
├── vpc.tf                # VPC and networking
├── security-groups.tf     # Security group rules
├── rds.tf                # RDS database configuration
├── ec2.tf                # EC2 and Auto Scaling Group
├── load-balancer.tf       # Application Load Balancer
├── cloudwatch.tf          # Monitoring and alarms
├── outputs.tf             # Output values
├── user_data.sh           # EC2 startup script
├── terraform.tfvars.example # Example variables
└── README.md              # This file
```

## Cost Optimization

The infrastructure uses cost-effective resources:

- **EC2**: t3.micro instances (eligible for free tier)
- **RDS**: db.t3.micro instance (eligible for free tier)
- **Load Balancer**: Application Load Balancer (minimal cost)
- **NAT Gateway**: 2 NAT Gateways for HA (~$45/month)

To reduce costs for development:

1. Set `desired_capacity = 1` and `min_size = 1`
2. Use single AZ by reducing subnet count
3. Disable Multi-AZ RDS by setting `multi_az = false`

## Cleanup

To destroy all resources and avoid charges:

```bash
terraform destroy
```

Type `yes` when prompted.

## Security Notes

- Database is in private subnets with no internet access
- Security groups follow least privilege principle
- Database credentials should be stored in AWS Secrets Manager for production
- Consider using SSL/TLS certificates for HTTPS

## Troubleshooting

### Common Issues

1. **Instances not healthy**: Check security groups and user data script
2. **Database connection failed**: Verify RDS security group allows EC2 access
3. **Load balancer 502 errors**: Ensure EC2 instances are running on port 3000

### Debugging Steps

1. Check Auto Scaling Group activity in AWS Console
2. SSH to instances to view logs: `pm2 logs todo-app`
3. Monitor CloudWatch logs: `/aws/ec2/todo-app`
4. Verify RDS connectivity from EC2 instances

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!
