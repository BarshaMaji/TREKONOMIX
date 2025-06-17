import streamlit as st

st.title("Plan Your Trip")

location = st.text_input("Destination")
days = st.number_input("Trip Duration (days)", min_value=1, step=1)
budget = st.number_input("Maximum Budget (INR)", min_value=1000)

if st.button("Show Recommendations"):
    st.session_state.search_params = {
        "location": location,
        "days": days,
        "budget": budget
    }
    st.switch_page("pages/2_Dashboard.py")
