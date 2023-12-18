import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the data
data = pd.read_csv('data_with_diffs.csv')

def fit_bayesian_model(y):
    X = sm.add_constant(np.ones(len(y)))  # adding a constant for intercept
    model = sm.GLM(y, X, family=sm.families.Gaussian())
    bayesian_results = model.fit_regularized()
    return bayesian_results.params

height_extremely_estimates = fit_bayesian_model(data[['diff_height_extremely', 'diff_height_extremely_2', 'diff_height_extremely_3', 'diff_height_extremely_4']].values.flatten())
print('Posterior parameter estimates for Effect of "Extremely" on Height:', height_extremely_estimates)

height_very_estimates = fit_bayesian_model(data[['diff_height_very', 'diff_height_very_2', 'diff_height_very_3', 'diff_height_very_4']].values.flatten())
print('Posterior parameter estimates for Effect of "Very" on Height:', height_very_estimates)

temp_extremely_estimates = fit_bayesian_model(data[['diff_temp_extremely', 'diff_temp_extremely_2']].values.flatten())
print('Posterior parameter estimates for Effect of "Extremely" on Temperature:', temp_extremely_estimates)

temp_very_estimates = fit_bayesian_model(data[['diff_temp_very', 'diff_temp_very_2']].values.flatten())
print('Posterior parameter estimates for Effect of "Very" on Temperature:', temp_very_estimates)
