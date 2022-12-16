from fastapi import FastAPI
import uvicorn
from pull_data import sample_generator

from new import get_sentiment


app = FastAPI()
# class Item(BaseModel):
#     sentiment: str
# import json

# reading the dataset
# import pandas as pd

# df = pd.read_csv(
#     "/workspaces/IDS706_Final_Project_klap/data/combined_movie_reviews.csv"
# )




# end points

# end point 1 : welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Review Application"}


# end point 2 : list a random row of the dataset
@app.get("/random")
async def get_random():
    return df.sample().to_dict("records")


@app.get("/movie_reviews/{source}/{size}")
async def source(source:str, size:int):
    movie_reviews = sample_generator(source,size)
    return {"movie_reviews":movie_reviews}


@app.get("/get_sentiment/{sentiment}")
async def getsent(sentiment:str):
   sentiment= sentiment(senti)
   return sentiment


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
