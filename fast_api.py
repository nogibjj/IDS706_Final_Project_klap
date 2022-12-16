from fastapi import FastAPI
import uvicorn
from pull_data import sample_generator
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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
    df = get_sent(review)
    result = open("result.txt", "r")
    return {"review":result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")