from fastapi import FastAPI


import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Weclome to the Movie Review Application"}

@app.get("/movies")
async def get_movies():
    return {"message": "List of all movies"}





if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')


