import streamlit as st
from pathlib import Path

# Inject background CSS
st.markdown(Path("background_style.css").read_text(), unsafe_allow_html=True)

st.title("🌍 Plan Your Dream Trip")
st.markdown("### Enter your preferences:")

with st.form("trip_form"):
    destination = st.text_input("Destination")
    days = st.number_input("Trip Duration (days)", min_value=1, value=3)
    season = st.selectbox("Season", ["On-season", "Off-season"])
    transport = st.selectbox("Transport", ["Flight", "Train", "Bus"])
    stay = st.selectbox("Accommodation", ["Hotel", "Hostel", "Apartment"])
    activity = st.selectbox("Activity Type", ["Family", "Adventure", "Historical"])
    avg_cost = st.number_input("Estimated Avg Daily Cost", value=100)
    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    st.session_state.trip_data = {
        "destination": destination,
        "days": days,
        "season": season,
        "transport_type": transport,
        "accommodation_type": stay,
        "activity_type": activity,
        "avg_daily_cost": avg_cost
    }
    st.switch_page("pages/2_Trip_Overview.py")
