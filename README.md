# DS-GA 1019: Advanced Python in Data Science 
This repository is for collaboration and review of the final project. 

This project implemented the backend of a movie recommender system based on movie metadata, user ratings, etc.

The dataset is from MovieLens: https://grouplens.org/datasets/movielens/latest/ 
The dataset and intermediate data are not pushed to Github due to file size limit. 

## Cleaning and Preprocess
1. Cleaning_movies.ipynb: cleans and preprocess movie metadata 
2. Cleaning_ratings.ipynb: cleans and preprocess user ratings data

## Text Vectorization and Dimension Reduction
1. Tfidf.ipynb: construct Tf-idf matrix of movie overviews
2. TSVD.ipynb: Truncated Singular Value Decomposition for reducing dimensions on TFIDF matrix 


## Pattern Learning  
1. movie_similarity.ipynb: movie similarity based on movie descriptions
2. Apriori_spark.ipynb: frequent set and association rules of user ratings, implemented on Spark
3. K_Means_spark.ipynb: K-Means clustering of movies based on movie descriptions 
