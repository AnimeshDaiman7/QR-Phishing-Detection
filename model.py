import pandas as pd
from sklearn.naive_bayes import GaussianNB
from feature_extraction import extract_features
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

X = []
y = data['label']

# Extract features
for url in data['url']:
    X.append(extract_features(url))

# Train model
model = GaussianNB()
model.fit(X, y)

print("✅ Model Trained Successfully")

# Save model
pickle.dump(model, open("model.pkl", "wb"))