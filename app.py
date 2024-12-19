import boto3

def create_ec2_instance():
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')

    # Define parameters for the EC2 instance
    instance_params = {
        'ImageId': 'ami-0614680123427b75e',  # Replace with your desired AMI ID
        'InstanceType': 't2.micro',         # Replace with your desired instance type
        'MinCount': 1,                      # Minimum number of instances
        'MaxCount': 1,                      # Maximum number of instances
        'KeyName': 'key-db',    # Replace with your key pair name
    }

    try:
        # Launch the EC2 instance
        response = ec2_client.run_instances(**instance_params)
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 Instance created successfully! Instance ID: {instance_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_ec2_instance()

