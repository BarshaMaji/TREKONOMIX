import streamlit as st

st.set_page_config(page_title="Trekonomix", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
            background-size: cover;
            background-position: center;
        }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌍 Trekonomix Travel Planner")
st.markdown("Welcome! Use the sidebar to explore your travel plan.")
