# using fast api to create a web app
#
# import the necessary libraries
from fastapi import FastAPI
import pandas as pd
import uvicorn
import os
import random



# create an instance of the FastAPI class
app = FastAPI()

# create a function that randomly generates sample of 1000 rows