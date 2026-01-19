import pandas as pd

df = pd.read_csv("race_data.csv")

# Keep only drivers with valid finishing positions
df = df[df['Position'].notna()]

# Ensure Position is integer
df['Position'] = df['Position'].astype(int)

# Create Top10 column correctly
df['Top10'] = df['Position'].apply(lambda x: 1 if x <= 10 else 0)

# Keep only relevant columns
df = df[['DriverNumber','Abbreviation','GridPosition','Top10']]

# Save final dataset
df.to_csv("final_data.csv", index=False)

print("Data prepared correctly for training")
