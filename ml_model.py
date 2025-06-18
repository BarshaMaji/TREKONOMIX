import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neural_network import MLPRegressor

# Load the dataset
df = pd.read_csv("trekonomix_dataset.csv")

# Define columns to encode and scale
label_cols = ['location', 'currency', 'month', 'accommodation_type', 
              'travel_purpose', 'traveler_type', 'tags', 'transport_options']
numeric_cols = ['average_days']

# Store encoders for later use
encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Normalize numeric columns
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Define features (X) and target (y)
X = df[label_cols + numeric_cols]
y = df['total_budget_on_season_INR']  # You can change to 'total_budget_off_season_INR' if needed

# Train the model
model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', max_iter=500, random_state=42)
model.fit(X, y)

# Save the model, encoders, and scaler
with open("ml_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model training complete. All files saved without modifying dataset.")
