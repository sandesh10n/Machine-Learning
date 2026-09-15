
# Label encodng : Conveting the labels into numeric form

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Loading the data from the csv file to pandas dataFrame

cancer_data = pd.read_csv("data.csv")

print(cancer_data.head())

# finding the count of different labels
print(cancer_data['diagnosis'].value_counts())

# Load the LabelEncoder function
label_encode = LabelEncoder()

labels = label_encode.fit_transform(cancer_data.diagnosis)

# Appending the labels to the DataFrame
cancer_data['target'] = labels

print(cancer_data.head())

print(cancer_data['target'].value_counts())