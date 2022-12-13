import pandas as pd

# append both datasets and save to new csv

df1 = pd.read_csv("data/imdb.csv")
df1["source"] = "imdb"
df2 = pd.read_csv("data/rotten_tomatoes.csv")
df2["source"] = "rotten_tomatoes"
df = df1.append(df2)
df.to_csv("data/combined_movie_reviews.csv", index=False)
