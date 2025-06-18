import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("trekonomix_dataset.csv")

# Encode categorical columns
label_cols = df.select_dtypes(include=['object']).columns.tolist()
encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str).str.lower())
    encoders[col] = le

# Features and label
X = df.drop(columns=["total_budget_on_season_INR"])
y = df["total_budget_on_season_INR"]

# Scale numeric columns
num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
scaler = MinMaxScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save everything
pickle.dump(model, open("rf_model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
