"""
Downloads a folder and files recursively from s3 - ONLY TESTED ON WINDOWS
"""
import os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
load_dotenv()

BUCKET = os.getenv('BUCKET')
FOLDER = os.getenv('FOLDER')

print('bucket: ', BUCKET)
print('folder: ', FOLDER)     

#initiate s3 resource
print('initiating s3 resource...')
s3 = boto3.client('s3')
# Define region
region = 'eu-west-1'

s3_resource = boto3.resource('s3')
local_dir = os.path.dirname(os.path.realpath(__file__)) + '/output/'

"""
Download the contents of a folder directory
Args:
    BUCKET: the name of the s3 bucket
    FOLDER: the folder path in the s3 bucket
    local_dir: a relative or absolute directory path in the local file system
"""
bucket = s3_resource.Bucket(BUCKET)
for obj in bucket.objects.filter(Prefix=FOLDER):
    target = obj.key if local_dir is None \
        else os.path.join(local_dir, os.path.relpath(obj.key, FOLDER))
    if not os.path.exists(os.path.dirname(target)):
        print('creating new directory')
        os.makedirs(os.path.dirname(target))
    if obj.key[-1] == '/':
        continue
    print('downloading file')
    bucket.download_file(obj.key, target)