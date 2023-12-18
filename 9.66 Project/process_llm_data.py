import pandas as pd
import pymc3 as pm
import numpy as np


# Load the CSV file
# Replace 'path_to_your_csv.csv' with the path to your CSV file
data = pd.read_csv('normalized_llm_data.csv')

# Compute the percentage increase for each pair
# The formula is: ((non_intensified - intensified) / intensified) * 100
columns_to_convert = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
for col in columns_to_convert:
    data.iloc[:, col] = pd.to_numeric(data.iloc[:, col], errors='coerce')

# Height with 'Extremely'
data['diff_height_extremely'] = ((data.iloc[:, 0] - data.iloc[:, 1]) / data.iloc[:, 1]) * 100
data['diff_height_extremely_2'] = ((data.iloc[:, 2] - data.iloc[:, 3]) / data.iloc[:, 3]) * 100
data['diff_height_extremely_3'] = ((data.iloc[:, 4] - data.iloc[:, 5]) / data.iloc[:, 5]) * 100
data['diff_height_extremely_4'] = ((data.iloc[:, 6] - data.iloc[:, 7]) / data.iloc[:, 7]) * 100

# Height with 'Very'
data['diff_height_very'] = ((data.iloc[:, 16] - data.iloc[:, 17]) / data.iloc[:, 17]) * 100
data['diff_height_very_2'] = ((data.iloc[:, 18] - data.iloc[:, 19]) / data.iloc[:, 19]) * 100
data['diff_height_very_3'] = ((data.iloc[:, 20] - data.iloc[:, 21]) / data.iloc[:, 21]) * 100
data['diff_height_very_4'] = ((data.iloc[:, 22] - data.iloc[:, 23]) / data.iloc[:, 23]) * 100

# Temperature with 'Extremely'
data['diff_temp_extremely'] = ((data.iloc[:, 8] - data.iloc[:, 9]) / data.iloc[:, 9]) * 100
data['diff_temp_extremely_2'] = ((data.iloc[:, 10] - data.iloc[:, 11]) / data.iloc[:, 11]) * 100

# Temperature with 'Very'
data['diff_temp_very'] = ((data.iloc[:, 12] - data.iloc[:, 13]) / data.iloc[:, 13]) * 100
data['diff_temp_very_2'] = ((data.iloc[:, 14] - data.iloc[:, 15]) / data.iloc[:, 15]) * 100

# Inspect the data
print(data.head())
data.to_csv("data_with_diffs.csv")