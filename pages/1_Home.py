import streamlit as st

st.title("🏠 Plan Your Trip")

with st.form("user_input_form"):
    destination = st.text_input("Destination")
    currency = st.selectbox("Currency", ["INR", "USD", "EUR", "YEN"])
    month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", 
                                   "July", "August", "September", "October", "November", "December"])
    accommodation_type = st.selectbox("Accommodation Type", ["Hotel", "Hostel", "Resort", "Apartment"])
    travel_purpose = st.selectbox("Travel Purpose", ["Business", "Vacation", "Backpacking", "Cultural"])
    traveler_type = st.selectbox("Traveler Type", ["Solo", "Couple", "Family", "Group"])
    tags = st.selectbox("Trip Tag", ["Adventure", "Luxury", "Budget", "Cultural"])
    transport_options = st.selectbox("Transport Option", ["Flight", "Train", "Bus"])
    average_days = st.number_input("Number of Days", 1, 30, 5)

    submitted = st.form_submit_button("Get Trip Overview")

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
    st.success("Redirecting to Trip Overview...")
    st.switch_page("pages/2_Trip_Overview.py")
