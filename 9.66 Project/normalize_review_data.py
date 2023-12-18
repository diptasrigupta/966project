import pandas as pd
import numpy as np

file_path = 'review_data.csv'
df = pd.read_csv(file_path)

df['Rating'] = df['Rating'].clip(lower=0.01)
df['Sqrt Rating'] = np.sqrt(df['Rating'])

df.to_csv('transformed_data.csv', index=False)
print(df.head())