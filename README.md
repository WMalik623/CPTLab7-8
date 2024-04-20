# CPTLab7-8
Wasil Fawad Malik - 2022623

Osaid Khan Afridi - 2022488


Model Information:

Model Type: Linear Regression

Model Architecture: The linear regression model assumes a linear relationship between the input features and the target variable. It tries to fit a straight line to the data.

Algorithm Used: Ordinary Least Squares (OLS) method is commonly used for estimating the parameters of the linear regression model.

Features: One feature (X) is used in this example, but it can be extended to multiple features.

Target Variable: Continuous variable (y)



Dataset Information:

Dataset Used: Synthetic dataset generated using make_regression function from scikit-learn.

Features: One feature (X) generated with random noise.

Target Variable: Continuous target variable (y) generated based on the input features.



Evaluation Metrics:

Evaluation Metric Used: Mean Squared Error (MSE)

Purpose: MSE measures the average squared difference between the actual and predicted values. Lower MSE indicates better model performance.



Initial Accuracy:

Initial Accuracy Metric: Mean Squared Error (MSE)

Initial Accuracy Value: 10%



Current Accuracy:

Current Accuracy Metric: Mean Squared Error (MSE)

Current Accuracy Value: 10%

# Feature Engineering:

In linear regression, feature engineering typically involves transforming or creating new features from the existing ones to better capture the relationship between the features and the target variable.
Since we have only one feature (X) in this example, we'll focus on techniques to enhance the predictive power of this single feature.
Polynomial Features: We can create polynomial features from the existing feature to capture non-linear relationships. This is done by adding powers of the existing feature to the dataset.
Interaction Terms: We can generate interaction terms by multiplying the existing feature with other features or with itself to capture interactions between features.
Normalization: Normalizing the features can sometimes improve the performance of linear regression models, especially when the features have different scales.
We use PolynomialFeatures to generate polynomial features up to degree 2 from the original feature X.
We then scale the polynomial features using StandardScaler to ensure that all features have the same scale.
Finally, we train a new linear regression model on the polynomial features and evaluate its performance using mean squared error.
Improved Accuracy: 15%
