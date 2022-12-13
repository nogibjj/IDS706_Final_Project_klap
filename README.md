# IDS706 Final Project
## Team: Kashaf Ali, Lorna Maria Aine, Pragya Raghuvanshi, and Aadila Jasmin

[![Python application test with Github Actions](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/IDS706_Final_Project_klap/actions/workflows/main.yml)


## HuggingFace Dataset ETL (Extraction, Transformation, Loading):
1. Build a search tool for looking for datasets
2. Build a datset inspection function
3. Click function for datasets "search" in hf_dataset_query.py: chmod +x hf_dataset_query.py
4. Add color to the click function results and use search click function with: ./hf-dataset-query.py query 'imdb' --limit 5 --sort True
5. Click function for datasets "inspection": ./hf_dataset_query.py inspect imdb --column train --rows 5
6. Load two datasets: "imdb" and "rotten_tomatoes" and save into two separate csv in the "data" directory using the save_to_csv function and save_datasets.py file. 


