import streamlit as st
import pandas as pd

with open("background_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏠 Plan Your Trip")

# Load dataset
df = pd.read_csv("trekonomix_dataset.csv")

# Safely extract unique values for dropdowns
def get_options(col):
    return sorted(df[col].dropna().unique().tolist())

# Dropdown options
locations = get_options("location")
currencies = get_options("currency")
months = get_options("month")
accommodations = get_options("accommodation_type")
purposes = get_options("travel_purpose")
traveler_types = get_options("traveler_type")
tags = get_options("tags")
transport_modes = get_options("transport_options")

with st.form("home_form"):
    destination = st.selectbox("Destination", locations)
    currency = st.selectbox("Currency", currencies)
    month = st.selectbox("Month", months)
    accommodation_type = st.selectbox("Accommodation Type", accommodations)
    travel_purpose = st.selectbox("Travel Purpose", purposes)
    traveler_type = st.selectbox("Traveler Type", traveler_types)
    tag = st.selectbox("Tags", tags)
    transport = st.selectbox("Transport Options", transport_modes)
    average_days = st.number_input("Days", min_value=1, value=3)

    submitted = st.form_submit_button("Next")

if submitted:
    st.session_state.user_input = {
        "location": destination,
        "currency": currency,
        "month": month,
        "accommodation_type": accommodation_type,
        "travel_purpose": travel_purpose,
        "traveler_type": traveler_type,
        "tags": tag,
        "transport_options": transport,
        "average_days": average_days
    }
    st.success("Redirecting to Trip Overview...")
    st.switch_page("pages/2_Trip_Overview.py")
