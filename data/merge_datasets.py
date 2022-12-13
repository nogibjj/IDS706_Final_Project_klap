import pandas as pd

# append both datasets and save to new csv
df1 = pd.read_csv("data/imdb.csv")
df2 = pd.read_csv("data/rotten_tomatoes.csv")
df = df1.append(df2)
df.to_csv("data/combined_move reviews.csv", index=False)
