import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('human_data.csv')

# columns
height_male = [0, 1, 2, 3, 16, 17, 18, 19]
height_female = [4, 5, 6, 7, 20, 21, 22, 23]
temperature = [8, 9, 10, 11, 12, 13, 14, 15,]

# data
mean_male = 69.2
std_dev_male = 2.66
mean_female = 64.3
std_dev_female = 2.58

mean_boston = 50.0
std_dev_boston = 15.61

# convert to numeric
for col in height_male + height_female + temperature :
    data.iloc[:, col] = pd.to_numeric(data.iloc[:, col], errors='coerce')

# Calculate Z-scores 
for col in height_male:
    data.iloc[:, col] = abs((data.iloc[:, col] - mean_male) / std_dev_male)


for col in height_female:
    data.iloc[:, col] = abs((data.iloc[:, col] - mean_female) / std_dev_female)

for col in temperature:
    data.iloc[:, col] = abs((data.iloc[:, col] - mean_boston) / std_dev_boston)


data.to_csv('normalized_human_data.csv')
import matplotlib.pyplot as plt


# sub_columns
height_male_extremely = [0, 2,]
height_male_none = [1, 3, 17, 19]
height_male_very = [ 16, 18, ]

height_female = [4, 5, 6, 7, 20, 21, 22, 23]

height_female_extremely = [4, 6,]
height_female_none = [5, 7, 21, 23]
height_female_very = [ 20, 22, ]


temperature_extremely = [8, 10,]
temperature_none = [9, 11, 13, 15,]
temperature_very = [12, 14,]

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def plot_kde(data, ax, label, color):
    data = np.array(data, dtype=float)
    data_clean = data[~np.isnan(data)]

    if len(data_clean) > 0:
        kde = gaussian_kde(data_clean)
        x_range = np.linspace(data_clean.min(), data_clean.max(), 500)
        y_values = kde(x_range)
        ax.plot(x_range, y_values, label=label, color=color)
        ax.fill_between(x_range, y_values, color=color, alpha=0.3) 

fig, axes = plt.subplots(2, 1, figsize=(8, 12))

# KDE for male height
plot_kde(data.iloc[3:, height_male_extremely + height_female_extremely].values.flatten(), axes[0], 'Extremely', 'red')
plot_kde(data.iloc[3:, height_male_very + height_female_very].values.flatten(), axes[0], 'Very', 'yellow')
plot_kde(data.iloc[3:, height_male_none + height_female_none].values.flatten(), axes[0], 'None', 'green')
axes[0].set_title('Height Distribution')
axes[0].set_xlabel('Height (Z-score)')
axes[0].set_ylabel('Density')
axes[0].legend()

# KDE for temperature
plot_kde(data.iloc[3:, temperature_extremely].values.flatten(), axes[1], 'Extremely', 'red')
plot_kde(data.iloc[3:, temperature_very].values.flatten(), axes[1], 'Very', 'yellow')
plot_kde(data.iloc[3:, temperature_none].values.flatten(), axes[1], 'None', 'green')
axes[1].set_title('Temperature Distribution')
axes[1].set_xlabel('Temperature (Z-score)')
axes[1].set_ylabel('Density')
axes[1].legend()


def mean(list):
    return sum(list)/len(list)

def diff(cols):
    arr = [ (data.iloc[3:, col1].mean() - data.iloc[3:, col2].mean()/data.iloc[3:, col2].mean()) * 100 for col1, col2 in cols]
    return mean(arr)
     
plt.tight_layout()
plt.savefig('figures/distributions_human_data.png')

# Calculate the differences for each category
diff_height_extremely = diff([(0, 1), (2, 3), (4, 5), (6, 7)])

diff_height_very =  diff([(16, 17), (18, 19), (20, 21), (22, 23)])

diff_temp_extremely = diff([(8, 9), (10, 11),])

diff_temp_very = diff([(12, 13), (14, 15),])

print(diff_height_extremely, diff_height_very, diff_temp_extremely, diff_temp_very)