import numpy as np
from sklearn.linear_model import LogisticRegression

# Generate random training data
np.random.seed(0)  # Set seed for reproducibility
X_train = np.random.randn(1, 5)  # Generate 100 samples with 2 features
y_train = np.random.randint(1, size=5)  # Generate random binary labels (0 or 1)

# Fit a logistic regression model
classifier = LogisticRegression().fit(X_train, y_train)

# Generate random test data
X_test = np.random.randn(5, 1)  # Generate 20 samples with 2 features

# Make predictions
predictions = classifier.predict(X_test)

# Show the predictions
print("Predictions:", predictions)
