# IDS706 Final Project
## Team: Kashaf Ali, Lorna Maria Aine, Pragya Raghuvanshi, and Aadila Jasmin

[![Python application test with Github Actions](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml)


![image](https://user-images.githubusercontent.com/111402572/208007750-2fd423a3-d927-43a3-ade1-79cf9c0f583d.png)



## HuggingFace Dataset ETL (Extraction, Transformation, Loading):
1. Build a search tool for looking for datasets
2. Build a datset inspection function
3. Click function for datasets "search" in hf_dataset_query.py: chmod +x hf_dataset_query.py
4. Add color to the click function results and use search click function with: ./hf-dataset-query.py query 'imdb' --limit 5 --sort True
5. Click function for datasets "inspection": ./hf_dataset_query.py inspect imdb --column train --rows 5
6. Load two datasets: "imdb" and "rotten_tomatoes" and save into two separate csv in the "data" directory using the save_to_csv function and save_datasets.py file. 
7. Merged two datasets to combined_movie_reviews.csv using merge_datasets.py

## [movie-reviews 0.0.2](https://github.com/lornamariak/movie-reviews)
1. Loaded combined_movie_reviews.csv 
2. created python package 
3. published to PyPI
4. used it generate records in the next step.

## NEXT STEPS - EDA & FASTAPI
1. Performed basic EDA on the merged dataset - EDA.py
2. Created data_generator.py function that returns only 1000 rows of the dataset (Can be used for AWS )
3. Created a FastAPI application - Uvicorn (Linked to the movie reviews dataset) with 4 endpoints:
    I. Displays Welcome message
    II. Returns Random Records - /random
    III. Returns a Random Negatively or Positively (0 or 1) labelled data row - /random/{0} or /random/{1}
    IV. Returns a review containing a particular word  - /find/{word}



