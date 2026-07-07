from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/model.pkl")

print("Model trained and saved successfully!")
