import streamlit as st
with open("background_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "admin" and password == "trek123":
        st.success("Logged in!")
    else:
        st.error("Invalid credentials.")
