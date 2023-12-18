import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Load the CSV file, skipping the first row
df = pd.read_csv('human_data.csv', skiprows=1)

# Convert the first two columns to numeric, ignoring non-numeric values
col1_numeric = pd.to_numeric(df.iloc[:, 0], errors='coerce').dropna()
col2_numeric = pd.to_numeric(df.iloc[:, 1], errors='coerce').dropna()

# Define the number of bins and calculate bin edges
bins = 100 - 48
bin_edges = np.linspace(48, 100, bins + 1)

# Plotting the histograms and KDE on separate plots
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Histograms
axes[0].hist(col1_numeric, bins=bin_edges, alpha=0.5, color='blue', edgecolor='k', label='Extremely short basketball player', density=True)
axes[0].hist(col2_numeric, bins=bin_edges, alpha=0.5, color='orange', edgecolor='k', label='Short basketball player', density=True)
axes[0].set_title('Histograms')
axes[0].set_xlim(48, 100)
axes[0].set_xlabel('Height (in)')
axes[0].set_ylabel('Frequency')
axes[0].legend()

# KDEs
kde_col1 = gaussian_kde(col1_numeric)
kde_col2 = gaussian_kde(col2_numeric)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
axes[1].fill_between(bin_centers, kde_col1(bin_centers), color='blue', alpha=0.5)
axes[1].fill_between(bin_centers, kde_col2(bin_centers), color='orange', alpha=0.5)
axes[1].set_title('KDE Plots')
axes[1].set_xlim(48, 100)
axes[1].set_xlabel('Height (in)')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.savefig('figures/extremely_short_basketball_comparison.png')
