import streamlit as st
with open("background_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏠 Plan Your Trip")

with st.form("home_form"):
    destination = st.text_input("Destination")
    currency = st.text_input("Currency")
    month = st.text_input("Month")
    accommodation_type = st.text_input("Accommodation Type")
    travel_purpose = st.text_input("Travel Purpose")
    traveler_type = st.text_input("Traveler Type")
    tags = st.text_input("Tags")
    transport_options = st.text_input("Transport Options")
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
        "tags": tags,
        "transport_options": transport_options,
        "average_days": average_days
    }
    st.success("Redirecting...")
    st.switch_page("pages/2_Trip_Overview.py")
