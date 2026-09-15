
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset to a Pandas Dataframe

dataset = pd.read_csv('Placement_Dataset.csv')

print(dataset.head())

print(dataset.shape)

print(dataset.isnull().sum())

# Analyse the distribution of data in the salary

# fig, ax = plt.subplots(figsize = (8, 8))

# sns.distplot(dataset.salary)
# plt.show()

dataset['salary'].fillna(dataset['salary'].median(), inplace=True)

print(dataset.isnull().sum())

# Filling missing values with mean values

# dataset['salary'].fillna(dataset['salary'].median(), inplace=True)

# Dropping missing values rows

salary_dataset = pd.read_csv('Placement_Dataset.csv')

print(salary_dataset.shape)

print(salary_dataset.isnull().sum())

salary_dataset = salary_dataset.dropna(how = 'any')
print(salary_dataset.isnull().sum())