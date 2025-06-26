# Main Terraform configuration for Todo App
# This file serves as the entry point for the Todo App infrastructure

# All resources are defined in separate files:
# - provider.tf: AWS provider configuration
# - variables.tf: Input variables
# - vpc.tf: VPC and networking resources
# - security-groups.tf: Security group configurations
# - rds.tf: RDS database configuration
# - ec2.tf: EC2 launch template and auto scaling group
# - load-balancer.tf: Application Load Balancer
# - cloudwatch.tf: CloudWatch monitoring and alarms
# - outputs.tf: Output values

# This modular approach makes the code more maintainable and easier to understand