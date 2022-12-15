import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = AWS_ACCESS_KEY_ID #From AWS Account
ACCESS_SECRET_KEY = AWS_SECRET_ACCESS_KEY #From AWS Account
BUCKET_NAME = 'klap-senti-bucket' #Add the Bucket name here

path = '/workspaces/IDS706_Final_Project_klap/sample.txt' #Ooperting system path where you want to upload the files/full path 
print(os.listdir(path))
for filename in os.listdir(path):
    data = open(path + '/' + filename, 'rb')
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
    os.remove(path + '/' + filename) 
    print("File Removed!")

print("Done")