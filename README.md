# IDS706 Final Project
## Team: Kashaf Ali, Lorna Maria Aine, Pragya Raghuvanshi, and Aadila Jasmin

[![Python application test with Github Actions](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml) [![AWS CodeBuild](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoieDE0Qkc1R1NqdEowaERYeXhmbThIVHZOeXJWLzFpTCtDZXUrU1dZMTJDNjFMaUZwMjhtMjhFeHg0Rnl1Q3VEWkU0ZzVHL3hLQXpmdzloTldxcFFPd3RZPSIsIml2UGFyYW1ldGVyU3BlYyI6IklQS1VGMVdHaVZrN3FwdWoiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

In this project, we used two Hugging Face datasets related to movie to conduct sentiment analysis using AWS S3, AWS Lambda and AWS Comprehend and build web microservice that has an API with Swagger Documentation and performs a query using a Pandas and returns useful information to the user.

![image](https://user-images.githubusercontent.com/67281453/208021407-1e37af79-cb6a-4fae-9564-744e256178e1.png)

## METHODOLOGY

1) Extraction of the Data from Hugging Face, Transformation and Loading to be used in codespace.
2) Pulling in the package that we created from https://github.com/lornamariak/reviews
3) Using FASTAPI to create an application that returns a JSON Payload to the User
4) The end-points are linked to AWS Lambda to perform sentiment analysis.


## HuggingFace Dataset ETL (Extraction, Transformation, Loading):
1. Build a search tool for looking for datasets
2. Build a datset inspection function
3. Click function for datasets "search" in hf_dataset_query.py: chmod +x hf_dataset_query.py
4. Add color to the click function results and use search click function with: ./hf-dataset-query.py query 'imdb' --limit 5 --sort True
5. Click function for datasets "inspection": ./hf_dataset_query.py inspect imdb --column train --rows 5
6. Load two datasets: "imdb" and "rotten_tomatoes" and save into two separate csv in the "data" directory using the save_to_csv function and save_datasets.py file. 
7. Merged two datasets to combined_movie_reviews.csv using merge_datasets.py

## Building a Python Package: [movie-reviews 0.0.2](https://github.com/lornamariak/movie-reviews)
1. Loaded combined_movie_reviews.csv 
2. created python package 
3. published to PyPI
4. used it generate records in the next step.

## NEXT STEPS - EDA & FASTAPI
1. Performed basic EDA on the merged dataset - EDA.py
2. Created data_generator.py function that returns only 1000 rows of the dataset (Can be used for AWS )
3. Created a FastAPI application - Uvicorn (Linked to the movie reviews dataset) with 6 endpoints: \
    I. Displays Welcome message\
    II. Returns Random Records - /random\
    III. Returns a Random Negatively or Positively (0 or 1) labelled data row - /random/{0} or /random/{1}\
    IV. Returns a review containing a particular word  - /find/{word}
    V. An endpoint, /movie_reviews/{source}/{size}, that pulls response reviews based on the source and number as specified by Client. This is also used to upload the file to the S3 bucket and perform analysis using Amazon Comprehend. 
    VI. Sentiment analysis performed using FastAPI endpoint, /tests/{r}, is created for a function that receives the user’s inputted list of text and runs it through the AWS Lambda to perform analysis. for predicted classifications.
  
## Sentiment Analysis using AWS S3, Lambda and Comprehend



## FastAPI Connection to AWS



## Continuous Integration & Continuous Delivery
1. Continuous Integration: We have Github Actions to ensure with CI with every commit, and we also use a Makefile to manually check this.
2. Continuous Delivery: We used an ECR Repository and CodeBuild to ensure CD (due to resource constraints we were not able to keep it live, but our build was successful).

<img width="397" alt="image" src="https://user-images.githubusercontent.com/111402572/208028248-b44a9a6a-762d-4ff1-aa0e-a95084a53401.png">




## THANK YOU!



