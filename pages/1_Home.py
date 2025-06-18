import streamlit as st
import pandas as pd
from ai_helper import predict_budget

df = pd.read_csv("trekonomix_dataset.csv")
st.title("🌍 Plan Your Trip")

col1, col2 = st.columns(2)
location = col1.selectbox("Destination", df["location"].unique())
currency = col2.selectbox("Currency", df["currency"].unique())
month = col1.selectbox("Month", df["month"].unique())
accommodation = col2.selectbox("Accommodation", df["accommodation_type"].unique())
travel_purpose = col1.selectbox("Travel Purpose", df["travel_purpose"].unique())
traveler_type = col2.selectbox("Traveler Type", df["traveler_type"].unique())
tags = col1.selectbox("Tags", df["tags"].unique())
transport = col2.selectbox("Transport", df["transport_options"].unique())

days = st.slider("Average Days", 1, 30, 5)
ex_rate = st.number_input("Exchange Rate to INR", value=1.0)
hotel_cost_on = st.number_input("Hotel Cost (On-season INR)", value=5000.0)
hotel_cost_off = st.number_input("Hotel Cost (Off-season Local)", value=4000.0)
trans_cost_on = st.number_input("Transport Cost (On-season INR)", value=3000.0)
trans_cost_off = st.number_input("Transport Cost (Off-season INR)", value=2500.0)
extra_exp_inr = st.number_input("Extra Expenses (INR)", value=1000.0)
extra_exp_local = st.number_input("Extra Expenses (Local)", value=800.0)

if st.button("🚀 Get Budget Recommendation"):
    user_input = {
        "location": location,
        "currency": currency,
        "month": month,
        "exchange_rate_to_INR": ex_rate,
        "accommodation_type": accommodation,
        "travel_purpose": travel_purpose,
        "traveler_type": traveler_type,
        "tags": tags,
        "average_days": days,
        "hotel_cost_on_season_INR": hotel_cost_on,
        "hotel_cost_off_season_local": hotel_cost_off,
        "transport_options": transport,
        "transport_cost_on_season_INR": trans_cost_on,
        "transport_cost_off_season_INR": trans_cost_off,
        "extra_expenses_INR": extra_exp_inr,
        "extra_expenses_local": extra_exp_local
    }
    cost_on, cost_off = predict_budget(user_input)
    st.success(f"✨ On-season Estimated Budget: ₹{cost_on}")
    st.success(f"🍃 Off-season Estimated Budget: ₹{cost_off}")
