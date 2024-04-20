from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Generate some synthetic data for demonstration
X, y = make_regression(n_samples=100, n_features=1, noise=0.5, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predictions
predictions = model.predict(X)

# Evaluate the model (MSE)
mse = mean_squared_error(y, predictions)
print("Mean Squared Error:", mse)
