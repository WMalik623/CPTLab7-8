from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Define the range of alpha values to try
alphas = [0.1, 1, 10, 100]

# Create a dictionary with the hyperparameters
param_grid = {'alpha': alphas}

# Create a Ridge regression model
ridge_model = Ridge()

# Perform grid search cross-validation
grid_search = GridSearchCV(ridge_model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit
