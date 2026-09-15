
import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# loading the dataset
dataset = sklearn.datasets.load_breast_cancer()

#print(dataset)

# loading the dataset to a pandas dataframe

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)

print(df.head())

print(df.shape)

X = df
Y = dataset.target

# print(X)
# print(Y)

# Splitting the data into training data and test data

X_train, X_test,  Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)

print(X.shape, X_train.shape, X_test.shape)

# Stadardize the data

print(dataset.data.std())

scaler = StandardScaler()

scaler.fit(X_train)

X_train_standardized = scaler.transform(X_train)

print(X_train_standardized)

X_test_standardized = scaler.transform(X_test)

print(X_train_standardized.std())


