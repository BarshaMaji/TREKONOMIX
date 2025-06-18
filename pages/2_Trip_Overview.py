import streamlit as st
from pathlib import Path
from ai_helper import predict_cost
from maps_helper import generate_map
from web_image_helper import fetch_web_images
from streamlit_folium import st_folium

# Inject background CSS
st.markdown(Path("background_style.css").read_text(), unsafe_allow_html=True)

st.title("🧳 Trip Overview")

if "trip_data" in st.session_state:
    user_input = st.session_state.trip_data
    destination = user_input["destination"]
    cost = predict_cost(user_input)

    st.success(f"Estimated Trip Cost: ₹{cost}")

    st.markdown("### Destination Map:")
    map_object = generate_map(destination)
    st_folium(map_object, width=700)

    st.markdown("### Explore Photos:")
    images = fetch_web_images(destination)
    for img in images:
        st.image(img, use_column_width=True)
else:
    st.warning("No trip data found. Please go back to the home page.")
