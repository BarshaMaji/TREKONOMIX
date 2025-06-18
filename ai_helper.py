import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("rf_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def predict_trip_cost(user_input):
    df = pd.DataFrame([user_input])
    for col in encoders:
        df[col] = encoders[col].transform(df[col].astype(str).str.lower())
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[num_cols] = scaler.transform(df[num_cols])
    prediction = model.predict(df)[0]
    return round(prediction, 2)
