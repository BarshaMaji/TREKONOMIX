import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("trekonomix_dataset.csv")

# Lowercase relevant categorical columns
categorical_cols = ['destination', 'season', 'transport_type', 'accommodation_type', 'activity_type']
for col in categorical_cols:
    df[col] = df[col].astype(str).str.lower()

# Label Encode
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Scale numeric
scaler = MinMaxScaler()
df[['days', 'avg_daily_cost']] = scaler.fit_transform(df[['days', 'avg_daily_cost']])

# Train model
X = df.drop(columns=['total_cost'])
y = df['total_cost']

model = LinearRegression()
model.fit(X, y)

# Save everything
with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
with open("cnn_model.h5", "wb") as f:
    pickle.dump(model, f)
