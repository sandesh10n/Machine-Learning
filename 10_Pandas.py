import pandas as pd
from sklearn.datasets import fetch_california_housing

housing_dataset = fetch_california_housing()

# print(type(housing_dataset))
# #print(housing_dataset)

# # Pandas Dataframe

california_df = pd.DataFrame(housing_dataset.data, columns = housing_dataset.feature_names)

# print(california_df.head())

# print(california_df.shape)

# Importing the data from a CSV file to a pandas Dataframe

diabetes_df = pd.read_csv('diabetes.csv')
#print(type(diabetes_df))

#print(diabetes_df.head())

#print(diabetes_df.tail)

#diabetes_df.info()

#print(diabetes_df.isnull().sum())

#counting the values based on the labels
#print(diabetes_df.value_counts('Outcome'))

# group the values based on the mean
#print(diabetes_df.groupby('Outcome').mean())

# Statistical Measures
print(california_df.mean())

print(california_df.std())

print(california_df.min())

print(california_df.describe())


