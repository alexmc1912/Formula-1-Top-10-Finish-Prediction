import pandas as pd
from joblib import load

# Load model and data
model = load("models/f1_model.joblib")
df = pd.read_csv("final_data.csv")

# Features and target
X = df[['GridPosition']]
y = df['Top10']

# Make predictions
df['PredictedTop10'] = model.predict(X)

# Map 1/0 to Yes/No for easy understanding
df['Top10'] = df['Top10'].map({1: 'Yes', 0: 'No'})
df['PredictedTop10'] = df['PredictedTop10'].map({1: 'Yes', 0: 'No'})

# Show simple table with driver abbreviation
print("\nDriver predictions (simplified view):")
print(df[['Abbreviation','GridPosition','Top10','PredictedTop10']].to_string(index=False))

# Calculate simple accuracy
accuracy = (df['Top10'] == df['PredictedTop10']).mean() * 100
print(f"\nModel Accuracy: {accuracy:.1f}%")
