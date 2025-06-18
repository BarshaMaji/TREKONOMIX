import streamlit as st
from streamlit_folium import st_folium
from ai_helper import predict_budget
from maps_helper import generate_map

st.title("📍 Plan Your Trip with Trekonomix")

with st.form("trip_form"):
    location = st.text_input("Destination", value="Goa")
    season = st.selectbox("Season", ["On-season", "Off-season"])
    stay = st.selectbox("Accommodation", ["Hotel", "Hostel", "Homestay"])
    purpose = st.selectbox("Purpose", ["Leisure", "Business", "Pilgrimage", "Adventure"])
    traveler = st.selectbox("Traveler Type", ["Solo", "Couple", "Family", "Group"])
    transport = st.selectbox("Transport Mode", ["Flight", "Train", "Bus", "Cab"])
    days = st.number_input("Average Days", min_value=1, value=5)
    extra = st.number_input("Estimated Extra Expenses (INR)", value=1000)

    submitted = st.form_submit_button("Calculate Budget")

if submitted:
    user_input = {
        "location": location,
        "season": season,
        "accommodation_type": stay,
        "travel_purpose": purpose,
        "traveler_type": traveler,
        "transport_options": transport,
        "average_days": days,
        "extra_expenses_INR": extra
    }

    budget = predict_budget(user_input)
    st.success(f"🎯 Predicted {season} Budget: ₹{budget}")
    st.markdown("### 🗺️ Trip Map")
    st_folium(generate_map(location), width=700)
