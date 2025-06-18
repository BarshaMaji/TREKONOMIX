# ai_helper.py

import numpy as np
import pickle
import pandas as pd

# Load model and encoders
model = pickle.load(open("cnn_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def predict_cost(user_input):
    df = pd.DataFrame([user_input])
    
    # Encode categorical
    for col in encoders:
        df[col] = encoders[col].transform(df[col].astype(str).str.lower())

    # Normalize numerical
    numeric_cols = ['average_days', 'hotel_cost_on_season_INR', 'hotel_cost_off_season_INR',
                    'transport_cost_on_season_INR', 'transport_cost_off_season_INR',
                    'extra_expenses_INR']
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Predict
    prediction = model.predict(df)[0]
    return round(prediction, 2)
