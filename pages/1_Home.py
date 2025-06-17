import streamlit as st

st.title("Welcome to Trekonomix 🚀")

st.header("Plan Your Dream Trip on a Budget")

with st.form("trip_form"):
    location = st.text_input("Enter your destination (e.g., Darjeeling)")
    budget = st.number_input("Enter your budget (₹)", min_value=1000, step=100)

    submitted = st.form_submit_button("Search Recommendations")

    if submitted:
        if not location or budget <= 0:
            st.error("Please provide valid destination and budget.")
        else:
            st.session_state.search_params = {
                "location": location,
                "budget": budget
            }
            st.success("Loading recommendations...")
            st.switch_page("pages/2_Dashboard.py")
