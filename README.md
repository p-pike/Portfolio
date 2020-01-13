# Portfolio

## What is in this repository ? 
- Churn dataset analysis
- Titanic dataset analysis
- Movie reviews dataset analysis

The purpose of these analyses is to find the model that best fits our problematics. For the Titanic dataset we want to predict if a passenger has survived. For the churn dataset we want to predict if a customer is going to leave for a competitor. For the movie reviews analysis we want to predict if a review is positive or negative. These are classification problems.

## How to run ?
To run a Jupyter Notebook you can use:
- Anaconda: https://www.anaconda.com/distribution/ (download link)

You must ensure that the python packages are installed with the correct version. For this purpose you can run the first cell in the importing librairies section.

**Note:** To avoid recomputing I have saved trained models in pickle files. But it is possible to redo the training, by setting the variable redo_training to true (in global variables). 

Dataset links:
- https://www.kaggle.com/becksddf/churn-in-telecoms-dataset/ (churn_dataset)
- https://www.kaggle.com/c/titanic/data (titanic_dataset)
- http://ai.stanford.edu/~amaas/data/sentiment/ (movie_reviews_dataset)
