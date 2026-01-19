# Formula 1 Top 10 Finish Prediction

A machine learning project that predicts whether a Formula 1 driver finishes in the Top 10 based on their starting grid position using real F1 race data collected from the FastF1 API.

## Project Overview

This project demonstrates a complete ML pipeline, from data collection to model evaluation, using Python and popular data/ML libraries. It uses FastF1 to fetch real race data, Pandas for preprocessing, and Scikit-learn's Random Forest model to make predictions. The output table clearly shows actual vs predicted results sorted by grid position.

The goal is to classify whether a driver will finish in the Top 10 of a race based on their starting position.

## Project Structure

Formula-1-Top-10-Finish-Prediction/
├── cache/ # FastF1 cache directory
├── models/ # Saved trained models
├── race_data.csv # Raw race data
├── final_data.csv # Processed dataset for ML
├── src/
│ ├── load_data.py # Fetches data from FastF1
│ ├── prepare_data.py # Cleans & labels data
│ ├── train_model.py # Trains the ML model
│ └── evaluate_model.py # Evaluates model & prints results
├── README.md # Project documentation (this file)
├── requirements.txt # Python dependencies

bash
Copy code

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alexmc1912/Formula-1-Top-10-Finish-Prediction.git
   cd Formula-1-Top-10-Finish-Prediction
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create cache directory for FastF1:

bash
Copy code
mkdir cache
How to Run
Run the following commands in order:

bash
Copy code
python src/load_data.py
python src/prepare_data.py
python src/train_model.py
python src/evaluate_model.py
After running evaluate_model.py, you will see a table showing:

Driver abbreviation

Grid position

Actual Top 10 finish (Yes/No)

Predicted Top 10 finish (Yes/No)

Overall accuracy

Example Output
yaml
Copy code
Driver predictions (simplified view):
Abbreviation GridPosition Top10 PredictedTop10
         HAM            1   Yes            Yes
         VER            2   Yes            Yes
         RUS            3    No             No
... (more drivers)

Model Accuracy: 85.0%
Technologies Used
Python

FastF1 API for live F1 data

Pandas for data manipulation

Scikit-learn for machine learning

Random Forest Classifier for prediction

Key Features
Real race data collection

Clean and easy-to-understand output table

End-to-end ML pipeline

Easily reproducible results

Future Improvements
Include additional features such as qualifying performance, team, and tyre strategy

Explore more advanced models like gradient boosting or neural networks

Support prediction across multiple races
