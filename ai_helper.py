# ai_helper.py

import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

# Load model and preprocessing tools
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_cost(user_input):
    df = pd.DataFrame([user_input])

    # Encode
    for col in encoders:
        if col in df.columns:
            df[col] = encoders[col].transform(df[col].str.lower())

    # Normalize
    if 'days' in df.columns and 'avg_daily_cost' in df.columns:
        df[['days', 'avg_daily_cost']] = scaler.transform(df[['days', 'avg_daily_cost']])

    prediction = model.predict(df)[0]
    return round(prediction, 2)
