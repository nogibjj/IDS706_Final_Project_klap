"""The main file for the FastAPI application"""
from fastapi import FastAPI
import uvicorn
from pull_data import sample_generator
import pandas as pd

# import smart_open


df = pd.read_csv(
    "/workspaces/IDS706_Final_Project_klap/data/combined_movie_reviews.csv"
)


app = FastAPI()

# end point 1 : welcome message
@app.get("/")
async def root():
    """"This is the welcome message"""
    return {"message": "Welcome to the Movie Review Application"}


# end point 2 : list a random row of the dataset from sample_generator

@app.get("/movie_reviews/{source}/{size}")
async def site(source: str, size: int):
    """"This is the random movie review generator"""""
    movie_reviews = sample_generator(source, size)
    return {"movie_reviews": movie_reviews}


# save response to a file
# @app.get("/save/{review}")
# async def save(review: str):
#     """"This is the save function"""""
#     file = open("review.txt", "w", encoding="utf-8")
#     file.write(review)
#     file.close()
#     # sending the file to s3
#     df_send = pd.read_csv("review.txt")
#     df_send.to_csv(
#         "s3://myklapbucket/file.txt",
#         storage_options={"key": aws_access_key_id, "secret": aws_secret_access_key},
#     )
#     # pulling the file from s3
#     df_pull = pd.read_csv(
#         smart_open("s3://projecttwitterbot/Searching/search_df.csv"),
#         lineterminator="\n",
#     )
#     result = print(df_pull)
#     return {"review": result}


@app.get("/tests/{r}")
async def tests(r: str):
    with open("r.txt", "w", encoding="UTF-8") as file:
        file.write(r)
    # read t.txt file
    with open("t.txt", "r", encoding="UTF-8") as df_pull:
        result = df_pull.read()
    # # save output of the dataframe to a variable
    # result = df_pull.read()
    # df_pull.close()
    return {"review": result}

# end point 2 : list a random row of the dataset
@app.get("/random")
async def get_random():
    return df.sample().to_dict("records")

# end point 3: list a random row of the dataset with a specific label 0 or 1 (negativw or positive)
@app.get("/random/{label}")
async def get_random_label(label: int):
    return df[df["label"] == label].sample(1).to_dict("records")


# end point 4: list a random row of the dataset with text containing specific word
@app.get("/find/{word}")
async def get_random_word(word: str):
    return df[df["text"].str.contains(word)].sample(1).to_dict("records")

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
