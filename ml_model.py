import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv("trekonomix_dataset.csv")

label_cols = ['location', 'currency', 'month', 'accommodation_type',
              'travel_purpose', 'traveler_type', 'tags', 'transport_options']
encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str).str.lower())
    encoders[col] = le

scaler = MinMaxScaler()
df[['average_days']] = scaler.fit_transform(df[['average_days']])

X = df[label_cols + ['average_days']]
y = df['total_budget_on_season_INR']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("ml_model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("✅ ML model trained and saved.")
