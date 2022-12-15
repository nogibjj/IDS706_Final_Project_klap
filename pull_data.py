# import pandas as pd
# from reviews.src.movie_reviews.generate_reviews import generate
from movie_reviews import generate

# # create a function that randomly generates sample of 10 rows from the imdb dataset
def sample_generator(source, size):
    df_sample = generate.generate_reviews(source, size)
    # remove label column from df_sample
    df_sample = df_sample.drop(columns=["label"])
    return df_sample


file = sample_generator("imdb", 1)
# save file as txt
file.to_csv("sample.txt", sep="\t", index=False)


# if __name__ == "__main__":
#     print(sample_generator())
# generate a random sample of 5 rows from source = imdb and 5 rows from source = rt
# def sample_generator2():
#     df_sample2 = generate("imdb", 10)
#     df_sample3 = generate("rt", 10)
#     frames = [df_sample2, df_sample3]
#     df_sample4 = pd.concat(frames)
#     df_sample5 = df_sample4.sample(frac=1).reset_index()[["text", "label"]]
#     return df_sample5

# sample_generator2()
# df = generate("imdb", 10)
# print(df)

# using pandas to read the csv file
# df = pd.read_csv('combined_movie_reviews.csv')

# df.head()
#
# print(df)
# # # create a function that randomly generates sample of 1000 rows
# def sample_generator():
#     df_sample = df.sample(n=1000)
#     return df_sample

# sample_generator()
