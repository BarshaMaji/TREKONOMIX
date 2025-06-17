import streamlit as st

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful")
        st.switch_page("pages/1_Home.py")
    else:
        st.error("Incorrect username or password")
