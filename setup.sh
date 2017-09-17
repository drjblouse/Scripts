#! /bin/bash
set -e

echo $(date -u) "Installing python pip requirements..."
pip install -r requirements.pip

if [ ! -f ~/.aws/config ]; then
	echo $(date -u) "Configuring the AWS CLI..."
	aws configure
fi

if [ ! -f ~/.ssh/${DEV_KEY_NAME}.pem ]; then
	echo $(date -u) "Creating new dev ssh key pair..."
	aws ec2 create-key-pair \
	    --key-name ${DEV_KEY_NAME} \
	    --query 'KeyMaterial' \
	    --output text > ~/.ssh/${DEV_KEY_NAME}.pem

	echo $(date -u) "Updating ssh key file permissions..."
	chmod 400 ~/.ssh/${DEV_KEY_NAME}.pem
fi

echo $(date -u) "Setup complete!"
