import pandas as pd
import pickle

model_on = pickle.load(open("model_on.pkl", "rb"))
model_off = pickle.load(open("model_off.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def predict_budget(user_input):
    df = pd.DataFrame([user_input])
    
    for col in encoders:
        df[col] = encoders[col].transform(df[col])

    df[['average_days', 'extra_expenses_INR']] = scaler.transform(
        df[['average_days', 'extra_expenses_INR']]
    )

    if user_input['season'] == 'On-season':
        prediction = model_on.predict(df)[0]
    else:
        prediction = model_off.predict(df)[0]
    
    return round(prediction, 2)
