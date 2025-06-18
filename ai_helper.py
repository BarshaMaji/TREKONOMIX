# ai_helper.py

import pickle
import pandas as pd

# Load the saved model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load encoders and scaler
with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_cost(user_input):
    df = pd.DataFrame([user_input])

    # Encode categorical columns
    for col in encoders:
        if col in df.columns:
            df[col] = encoders[col].transform(df[col].str.lower())

    # Normalize numeric columns
    if 'days' in df.columns and 'avg_daily_cost' in df.columns:
        df[['days', 'avg_daily_cost']] = scaler.transform(df[['days', 'avg_daily_cost']])

    # Predict
    prediction = model.predict(df)[0]
    return round(prediction, 2)
