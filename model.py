# app/model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

def predict(features):
    """
    features: list of 4 numbers [sepal_length, sepal_width, petal_length, petal_width]
    """
    return int(model.predict([features])[0])