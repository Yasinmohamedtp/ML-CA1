from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Example dataset: stock levels and sales history
X, y = make_regression(n_samples=100, n_features=5, noise=0.1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# AutoML model
automl = TPOTRegressor(verbosity=2, generations=5, population_size=50)
automl.fit(X_train, y_train)

# Predictions and score
print(automl.score(X_test, y_test))
automl.export('inventory_model.py')
