import pandas as pd

# using pandas to read the csv file
df = pd.read_csv('combined_movie_reviews.csv')


df.head()


# create a function that randomly generates sample of 1000 rows
def sample_generator():
    df_sample = df.sample(n=1000)
    return df_sample

sample_generator()
