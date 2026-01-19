import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

df = pd.read_csv("final_data.csv")

X = df[["GridPosition"]]
y = df["Top10"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
dump(model, "models/f1_model.joblib")

print("Model trained and saved")
