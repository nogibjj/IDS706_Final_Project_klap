from datasets import list_datasets, load_dataset

# build a dataset search query
def search(query, limit=10, sort=True):
    """Search for a dataset by name or description"""

    # get all datasets that match the query
    datasets = [dataset for dataset in list_datasets() if query in dataset]
    sorted_datasets = sorted(datasets) if sort else datasets
    limited_result = sorted_datasets if limit is None else sorted_datasets[:limit]
    return limited_result

# inspect a dataset
def inspect_data(dataset, column="train", rows=5):
    """Inspect a dataset"""

    # load dataset
    dataset = load_dataset(dataset)
    # get first 5 rows of first split
    data = dataset[column][0:rows]
    return data


# save the loaded datasets to different csv files in a new directory
def save_to_csv(dataset, path, column="train"):
    """Save a dataset to csv"""

    # load dataset
    dataset = load_dataset(dataset)
    # get first 5 rows of first split
    data = dataset[column]
    # save to csv
    data.to_csv(path, index=False)
    return data

# # save the loaded dataset to csv in a new directory
# def save_to_csv(dataset, column="train"):
#     """Save a dataset to csv"""

#     # load dataset
#     dataset = load_dataset(dataset)
#     # get first 5 rows of first split
#     data = dataset[column]
#     # save to csv
#     data.to_csv("data.csv", index=False)
#     return data





# load rotten tomatoes dataset
# rotten_tomatoes = load_dataset("rotten_tomatoes")

# print the first row in the training set for the rotten tomatoes dataset
# print(rotten_tomatoes["train"][0])

