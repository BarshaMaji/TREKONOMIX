import streamlit as st
from recommend_trip import get_recommendations
from travel_api import get_travel_tip
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

st.title("Recommended Trips for You 🎒")

if "search_params" not in st.session_state:
    st.error("Please go to the Home page and enter your trip details.")
    st.stop()

params = st.session_state.search_params
results = get_recommendations(params["location"], params["budget"])

if results is None:
    st.warning("No trips found under your budget for that location.")
    st.stop()

geolocator = Nominatim(user_agent="trekonomix")
kolkata = (22.5726, 88.3639)

for i, trip in enumerate(results, 1):
    st.subheader(f"Option {i}: {trip['location']}")
    st.write(f"Travel Purpose: {trip.get('travel_purpose', 'N/A')}")
    st.write(f"Accommodation Type: {trip.get('accommodation_type', 'N/A')}")
    st.write(f"Mode of Transport: {trip.get('mode_of_transport', 'N/A')}")

    on_budget = trip['total_budget_on_season_INR']
    off_budget = trip['total_budget_off_season_INR']

    st.write(f"💸 On-season Budget: ₹{on_budget}")
    st.write(f"🍃 Off-season Budget: ₹{off_budget}")

    if off_budget < on_budget:
        st.success("🟢 Recommended Time: Off-season (Cheaper)")
    else:
        st.info("🟡 Recommended Time: On-season (Better Experience)")

    diff = abs(on_budget - off_budget)
    if diff >= 3000:
        st.info(f"Estimated Savings: ₹{diff} in cheaper season")

    st.info(f"🌟 Travel Tip: {get_travel_tip(trip['location'])}")

    # Map section
    dest = geolocator.geocode(trip["location"])
    if dest:
        dest_coords = (dest.latitude, dest.longitude)
    else:
        dest_coords = (20.5937, 78.9629)  # Default India center

    m = folium.Map(location=[(kolkata[0] + dest_coords[0]) / 2, (kolkata[1] + dest_coords[1]) / 2], zoom_start=5)
    folium.Marker(kolkata, tooltip="Kolkata", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker(dest_coords, tooltip=trip["location"], icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine([kolkata, dest_coords], color="green").add_to(m)

    st_folium(m, height=400, width=700)
    st.markdown("---")
