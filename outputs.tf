# Outputs
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "load_balancer_dns" {
  description = "DNS name of the load balancer"
  value       = aws_lb.main.dns_name
}

output "load_balancer_url" {
  description = "URL of the Todo App"
  value       = "http://${aws_lb.main.dns_name}"
}

output "database_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.main.endpoint
  sensitive   = true
}

output "autoscaling_group_name" {
  description = "Name of the Auto Scaling Group"
  value       = aws_autoscaling_group.main.name
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs of the private subnets"
  value       = aws_subnet.private[*].id
}

output "ssh_instructions" {
  description = "Instructions for SSH access to instances"
  value       = var.key_pair_name != "" ? "To SSH to instances: aws ssm start-session --target <INSTANCE-ID> or ssh -i ${var.key_pair_name}.pem ec2-user@<PRIVATE-IP>" : "No SSH key configured. Set key_pair_name variable to enable SSH access."
}

output "cloudwatch_dashboard_url" {
  description = "CloudWatch Dashboard URL"
  value       = "https://${var.aws_region}.console.aws.amazon.com/cloudwatch/home?region=${var.aws_region}#dashboards:name=${var.project_name}-dashboard"
}

output "application_port" {
  description = "Port number the application is running on"
  value       = var.app_port
}

output "application_port_range" {
  description = "Port range allowed for the application"
  value       = "${var.app_port_range.start}-${var.app_port_range.end}"
}
