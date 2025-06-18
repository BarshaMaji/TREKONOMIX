import streamlit as st

st.title("🔐 User Login")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32');
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "admin" and password == "trek123":
        st.success("Login successful! 🎉")
    else:
        st.error("Invalid credentials. Try again.")
