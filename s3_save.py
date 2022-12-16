import os

# import boto3
# from botocore.client import Config
# from smart_open import smart_open
import pandas as pd

# ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"  #From AWS Account
# ACCESS_SECRET_KEY = 'AWS_SECRET_ACCESS_KEY' #From AWS Account
BUCKET_NAME = "myklapbucket"  # Add the Bucket name here

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]


