import streamlit as st
from ai_helper import predict_cost
from maps_helper import generate_map
from streamlit_folium import st_folium
import requests

st.title("🧳 Trip Overview")

user_input = st.session_state.get("user_input", None)

if user_input:
    cost = predict_cost(user_input)
    st.success(f"Predicted Trip Cost: ₹{cost}")

    st.markdown("### 🌐 Destination Map")
    m = generate_map(user_input['location'])
    st_folium(m, width=700)

    # Web images
    st.markdown("### 📸 Destination Images")
    query = user_input["location"]
    url = f"https://source.unsplash.com/800x400/?{query},travel"
    st.image(url, use_column_width=True)
else:
    st.warning("Please enter your trip details on the Home page.")
