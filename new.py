import pandas as pd
import os
import json
import csv

# import boto3
# from botocore.client import Config
from smart_open import smart_open
import pandas as pd

# ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"  #From AWS Account
# ACCESS_SECRET_KEY = 'AWS_SECRET_ACCESS_KEY' #From AWS Account
BUCKET_NAME = "myklapbucket"  # Add the Bucket name here

aws_access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

df = pd.read_csv("sample.txt")

def get_sent(review):
    #senti_df= pd.read_json("review")
    #senti_csv= senti_df.to_csv("/workspaces/IDS706_Final_Project_klap/senti.csv")
    # review.to_csv(
    #     "s3://myklapbucket/senti.txt",
    #     storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key},
    # )
    # result_df = pd.read_csv(smart_open('s3://myklapbucket/results.csv'), lineterminator='\n')


def get_sentiment(review):
    print(review.dtype)
    print("This is working")
    result=positive
    return result

