import fastf1
import pandas as pd
import os

# Create cache folder if it doesn't exist
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

# Load race session
session = fastf1.get_session(2023, "Austin", "R")
session.load()

# Get relevant data
df = session.results[['DriverNumber','Abbreviation','GridPosition','Position']]

# Save cleaned data
df.to_csv("race_data.csv", index=False)
print("Race data loaded successfully!")
