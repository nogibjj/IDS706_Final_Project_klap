from datasets import load_dataset

# load rotten tomatoes dataset
rotten_tomatoes = load_dataset("rotten_tomatoes")

# print the first row in the training set for the rotten tomatoes dataset
print(rotten_tomatoes["train"][0])

