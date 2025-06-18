import streamlit as st
from ai_helper import predict_cost
from maps_helper import generate_map
from web_image_helper import fetch_web_images
from streamlit_folium import st_folium

with open("background_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🧳 Trip Overview")

ui = st.session_state.get("user_input")
if ui:
    cost = predict_cost(ui)
    st.success(f"✅ Estimated Trip Cost: ₹{cost}")

    st.markdown("### Map")
    st_folium(generate_map(ui["location"]), width=700)

    st.markdown("### Photos")
    for img in fetch_web_images(ui["location"]):
        st.image(img, use_column_width=True)
else:
    st.warning("Go to the homepage to enter trip details.")
