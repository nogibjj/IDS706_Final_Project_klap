
import os.path
import pandas as pd

#open file 
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path,"./data/combined_movie_reviews.csv")
f = open(path)

#read it using pandas
data = pd.read_csv(f)

#function to generate mini data sets
def generate(source:str, size:int):
    """
    generate a sample dataset using generate(source, sample size):
    source can be imdb or rt for rotten tomatoes - string
    sample size can be any number between 1 and max rows of the dataset 
    default sample size is 30 records #not set yet
    returns a pandas object as dataframe
    """
    source = str(source)
    if size < 1:
       raise Exception(f"Sample size must be greater than {size}")
    elif size > data.shape[0]:
        raise Exception(f"Sample size must be greater than {size}")
    else:
        pass
    
    tmp = data[(data["source"] == source)]
    reviews = tmp.sample(size)
    return reviews
