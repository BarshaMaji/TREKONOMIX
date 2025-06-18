import streamlit as st
st.set_page_config(page_title="Trekonomix", layout="wide")
with open("background_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.title("🏝️ Welcome to Trekonomix")
st.markdown("### Your AI-powered travel budget planner")
st.markdown("Use the sidebar to start planning your trip.")
