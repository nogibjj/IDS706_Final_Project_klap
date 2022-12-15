from fastapi import FastAPI
import uvicorn
import json
# reading the dataset
import pandas as pd
df = pd.read_csv('/workspaces/IDS706_Final_Project_klap/data/combined_movie_reviews.csv')

app = FastAPI()


# end points

# end point 1 : welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Review Application"}

# end point 2 : list a random row of the dataset 
@app.get("/random")
async def get_random():
    return df.sample().to_dict('records')

# end point 3: list a random row of the dataset with a specific label 0 or 1 (negativw or positive)
@app.get("/random/{label}")
async def get_random_label(label: int):
    return df[df['label'] == label].sample(1).to_dict('records')


# end point 4: list a random row of the dataset with text containing specific word
@app.get("/find/{word}")
async def get_random_word(word: str):
    return df[df['text'].str.contains(word)].sample(1).to_dict('records')


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')


