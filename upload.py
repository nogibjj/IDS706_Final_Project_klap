"""Load reviews in S3 bucket"""
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

df = pd.read_csv("sample.txt")

df.to_csv(
    "s3://myklapbucket/file.txt",
    storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key},
)

# df2 = pd.read_csv("review.txt")

# def get_sent(review):
#     review.to_csv(
#         "s3://myklapbucket/file.txt",
#         storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key},
#     )
#     result_df = pd.read_csv(
#         smart_open("s3://myklapbucket/results.csv"), lineterminator="\n"
#     )

# sentiment = get_sent(df)


# path = '/workspaces/IDS706_Final_Project_klap' #Ooperting system path where you want to upload the files/full path
# print(os.listdir(path))
# for filename in os.listdir(path):
#     data = open(path + '/' + filename, 'rb')
#     s3 = boto3.resource(
#         's3',
#         aws_access_key_id="ACCESS_KEY_ID",
#         aws_secret_access_key="ACCESS_SECRET_KEY",
#         config=Config(signature_version='s3v4')
#     )
#     s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
#     os.remove(path + '/' + filename)
#     print("File Removed!")

# print("Done")
def get_sent():
    with open("t.txt", "r", encoding="UTF-8") as df_pull:   
        result = df_pull.read()
    return result