import pandas as pd
import pickle

# Load model and preprocessors
model = pickle.load(open("ml_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Define column lists used in the model
label_cols = ['location', 'currency', 'month', 'accommodation_type', 
              'travel_purpose', 'traveler_type', 'tags', 'transport_options']
numeric_cols = ['average_days']

def predict_cost(user_input):
    """
    user_input: dict with keys matching required features
    Example:
    {
        'location': 'Paris',
        'currency': 'EUR',
        'month': 'June',
        'accommodation_type': 'Hotel',
        'travel_purpose': 'Vacation',
        'traveler_type': 'Family',
        'tags': 'Cultural',
        'transport_options': 'Flight',
        'average_days': 5
    }
    """

    df = pd.DataFrame([user_input])

    # Encode categorical features
    for col in label_cols:
        df[col] = encoders[col].transform(df[col].astype(str))

    # Scale numeric features
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Predict total cost
    prediction = model.predict(df)[0]
    return round(prediction, 2)
