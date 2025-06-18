import numpy as np
import pickle
import pandas as pd

# Load model and tools
model = pickle.load(open("cnn_model.h5", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def safe_encode(col_name, value):
    encoder = encoders[col_name]
    classes = encoder.classes_.tolist()
    value = value.lower()
    if value in classes:
        return encoder.transform([value])[0]
    else:
        # Add fallback to first class or unknown label
        return 0

def predict_cost(user_input):
    # Preprocess
    df = pd.DataFrame([user_input])
    for col in encoders:
        df[col] = [safe_encode(col, df[col].values[0])]
    
    df[['days', 'avg_daily_cost']] = scaler.transform(df[['days', 'avg_daily_cost']])
    
    pred = model.predict(df)[0]
    return round(pred, 2)
