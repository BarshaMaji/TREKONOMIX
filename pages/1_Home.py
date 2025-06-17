import streamlit as st

st.set_page_config(page_title="Trekonomix", layout="centered")

st.title("Welcome to Trekonomix 🌍")
st.markdown("### Plan your trip based on your budget!")

location = st.text_input("Enter Destination")
budget = st.number_input("Enter Budget (INR)", min_value=0)

if st.button("Search"):
    if not location or not budget:
        st.warning("Please fill all fields.")
    else:
        st.session_state.search_params = {
            "location": location,
            "budget": budget
        }
        st.success("Search parameters saved. Go to Dashboard ➡️")
