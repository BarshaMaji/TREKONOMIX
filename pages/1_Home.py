import streamlit as st
from PIL import Image

# Optional: Set background or logo
st.image("trekonomix_logo.png", use_column_width=True)

st.title("Plan Your Perfect Trip with Trekonomix 🧳")

# Input form
with st.form("trip_form"):
    destination = st.text_input("Where do you want to go?", placeholder="e.g., Darjeeling")
    no_of_days = st.number_input("For how many days?", min_value=1, max_value=30, step=1)
    budget = st.number_input("What's your total budget (in INR)?", min_value=1000)

    submitted = st.form_submit_button("Search Trips")

# Save inputs to session state and switch to dashboard
if submitted:
    if not destination or not budget:
        st.warning("Please fill in all fields.")
    else:
        st.session_state.search_params = {
            "location": destination,
            "days": no_of_days,
            "budget": budget
        }
        st.success("Finding the best options for you... 🧠")
        st.switch_page("pages/2_Dashboard.py")
