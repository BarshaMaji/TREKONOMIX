import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("trekonomix_dataset.csv")

# Encode all categorical columns
label_cols = ['location', 'currency', 'month', 'accommodation_type', 'travel_purpose', 'traveler_type', 'tags', 'transport_options']
encoders = {}

for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features for training
features = ['location', 'currency', 'month', 'exchange_rate_to_INR', 'accommodation_type',
            'travel_purpose', 'traveler_type', 'tags', 'average_days',
            'hotel_cost_on_season_INR', 'hotel_cost_off_season_local', 'transport_options',
            'transport_cost_on_season_INR', 'transport_cost_off_season_INR',
            'extra_expenses_INR', 'extra_expenses_local']

X = df[features]
y_on = df['total_budget_on_season_INR']
y_off = df['total_budget_off_season_INR']

# Train/test split
X_train, X_test, y_train_on, y_test_on = train_test_split(X, y_on, test_size=0.2, random_state=42)
_, _, y_train_off, y_test_off = train_test_split(X, y_off, test_size=0.2, random_state=42)

# Train Random Forest models
model_on = RandomForestRegressor()
model_on.fit(X_train, y_train_on)

model_off = RandomForestRegressor()
model_off.fit(X_train, y_train_off)

# Save models and encoders
with open("rf_model_on.pkl", "wb") as f:
    pickle.dump(model_on, f)
with open("rf_model_off.pkl", "wb") as f:
    pickle.dump(model_off, f)
with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)
