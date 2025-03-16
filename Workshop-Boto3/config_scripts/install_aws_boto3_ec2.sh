#Install AWS Boto3 in EC2 machine
sudo yum update -y
sudo yum install -y python3-pip python3 python3-setuptools
pip3 install boto3 --user

#Para que boto3 funcione hay que instalar algo llamado AWS CLI en la maquina:
sudo yum install python -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
aws –version