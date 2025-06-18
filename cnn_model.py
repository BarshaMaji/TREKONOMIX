import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neural_network import MLPRegressor
import pickle

# Load dataset
df = pd.read_csv("trekonomix_dataset.csv")

# Select relevant columns
features = [
    'location', 'accommodation_type', 'travel_purpose', 'traveler_type',
    'transport_options', 'average_days', 'extra_expenses_INR'
]
target_on = 'total_budget_on_season_INR'
target_off = 'total_budget_off_season_INR'

# Encode categorical columns
encoders = {}
for col in ['location', 'accommodation_type', 'travel_purpose', 'traveler_type', 'transport_options']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Scale numerical columns
scaler = MinMaxScaler()
df[['average_days', 'extra_expenses_INR']] = scaler.fit_transform(df[['average_days', 'extra_expenses_INR']])

# Train separate models
X = df[features]
y_on = df[target_on]
y_off = df[target_off]

model_on = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=1000, random_state=42)
model_off = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=1000, random_state=42)

model_on.fit(X, y_on)
model_off.fit(X, y_off)

# Save models and encoders
pickle.dump(model_on, open("model_on.pkl", "wb"))
pickle.dump(model_off, open("model_off.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
