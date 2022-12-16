from fastapi import FastAPI
import uvicorn
from pull_data import sample_generator
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
import smart_open

app = FastAPI()

# end point 1 : welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Review Application"}

# end point 2 : list a random row of the dataset from sample_generator
@app.get("/movie_reviews/{source}/{size}")
async def source(source:str, size:int):
    movie_reviews = sample_generator(source,size)
    return {"movie_reviews":movie_reviews}

# save response to a file
@app.get("/save/{review}")
async def save(review:str):
    file = open("review.txt", "w")
    file.write(review)
    file.close()
    #sending the file to s3
    df_send = pd.read_csv("review.txt")
    df_send.to_csv(
    "s3://myklapbucket/file.txt",
    storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key},)
    #pulling the file from s3
    df_pull = pd.read_csv(smart_open('s3://projecttwitterbot/Searching/search_df.csv'), lineterminator='\n')
    result = print(df_pull)
    return {"review":result}


@app.get("/tests/{r}")
async def tests(r:str):
    file = open("r.txt", "w")
    file.write(r)
    file.close()
    #read t.txt file 
    df_pull = open("t.txt", "r")
    # save output of the dataframe to a variable
    result = df_pull.read()
    df_pull.close()
    return {"review":result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")