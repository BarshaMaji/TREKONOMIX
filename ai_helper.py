import pandas as pd
import pickle

model_on = pickle.load(open("rf_model_on.pkl", "rb"))
model_off = pickle.load(open("rf_model_off.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

def predict_budget(user_input):
    df = pd.DataFrame([user_input])
    for col in encoders:
        df[col] = encoders[col].transform(df[col])
    prediction_on = model_on.predict(df)[0]
    prediction_off = model_off.predict(df)[0]
    return round(prediction_on, 2), round(prediction_off, 2)
