#!/bin/bash
sudo su
# Log everything
exec > >(tee /var/log/user-data.log) 2>&1

# Update system
yum update -y

# Install basic tools
sudo yum install -y git curl

# Download and execute the full setup script from GitHub
cd /tmp
sudo curl -fsSL https://raw.githubusercontent.com/rtcapoquian/test/main/setup.sh -o setup.sh
sudo chmod +x setup.sh

# Execute setup with database parameters and port
./setup.sh "${db_endpoint}" "${db_name}" "${db_username}" "${db_password}" "${app_port}"
