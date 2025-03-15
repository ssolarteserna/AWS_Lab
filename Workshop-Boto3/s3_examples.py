import boto3

# Initialize the S3 client (no region specified)
s3 = boto3.client('s3')

# or with specific region
#s3 = boto3.client('s3', region_name='us-east-1')

def list_buckets():
    """Lists all S3 buckets in your account."""
    try:
        response = s3.list_buckets()
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing buckets: {e}")

def create_bucket(bucket_name, region):
    """Creates a new S3 bucket. Bucket name must be globally unique."""
    try:
        s3_client = boto3.client('s3', region_name=region)
        response = s3_client.create_bucket(
            Bucket=bucket_name
        )
        print(f"response: {response}")
        print(f"Bucket '{bucket_name}' created in region '{region}'")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_file(file_name, bucket, object_name=None):
    """Uploads a file to an S3 bucket. If object_name is not specified, file_name is used."""
    if object_name is None:
        object_name = file_name
    try:
        response = s3.upload_file(file_name, bucket, object_name)
        print(f"response: {response}")
        print(f"File '{file_name}' uploaded to '{bucket}/{object_name}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file(bucket, object_name, file_name):
    """Downloads a file from an S3 bucket."""
    try:
        s3.download_file(bucket, object_name, file_name)
        print(f"File '{object_name}' downloaded from '{bucket}' to '{file_name}'")
    except Exception as e:
        print(f"Error downloading file: {e}")

def list_objects(bucket):
    """Lists objects within an S3 bucket."""
    try:
        response = s3.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            print(f"Objects in '{bucket}':")
            for obj in response['Contents']:
                print(f"  - {obj['Key']}")
        else:
            print(f"Bucket '{bucket}' is empty.")
    except Exception as e:
        print(f"Error listing objects: {e}")

def delete_object(bucket, object_name):
    """Deletes an object from an S3 bucket."""
    try:
        s3.delete_object(Bucket=bucket, Key=object_name)
        print(f"Object '{object_name}' deleted from '{bucket}'")
    except Exception as e:
        print(f"Error deleting object: {e}")


def delete_bucket(bucket, region):
    """
    Deletes an S3 bucket. The bucket MUST be empty first.
    """
    try:
        s3_client = boto3.client('s3', region_name=region)
        s3_client.delete_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' deleted")
    except Exception as e:
        print(f"Error deleting bucket: {e}")


# Example Usage
if __name__ == "__main__":
    # Replace with your actual values:
    bucket_name = "llanobucketmar032024-v2"
    region = "us-east-1"
    file_name = "otroarchivo.txt"
    object_name = "s3_otroarchivo_object.txt"

    # Create a test file
    with open(file_name, "w") as f:
        f.write("This is a test file.")

    list_buckets()
    # create_bucket(bucket_name, region) # Uncomment this to create the bucket (if needed)
    # upload_file(file_name, bucket_name, object_name)
    # list_objects(bucket_name)
    # download_file(bucket_name, object_name, "downloaded_file.txt")
    # delete_object(bucket_name, object_name)
    # delete_bucket(bucket_name, region) #Uncomment this to delete the bucket but first is needed delete all objects