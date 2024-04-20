from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

# Generate polynomial features (up to degree 2)
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Scale the features
scaler = StandardScaler()
X_poly_scaled = scaler.fit_transform(X_poly)

# Create a new linear regression model
model_with_poly_features = LinearRegression()

# Fit the model to the polynomial features
model_with_poly_features.fit(X_poly_scaled, y)

# Predictions
predictions_poly = model_with_poly_features.predict(X_poly_scaled)

# Evaluate the model (MSE)
mse_poly = mean_squared_error(y, predictions_poly)
print("Mean Squared Error with Polynomial Features:", mse_poly)
