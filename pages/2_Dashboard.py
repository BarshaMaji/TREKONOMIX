import streamlit as st
from recommend_trip import get_recommendations
from travel_api import get_travel_tip
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

st.title("Recommended Trips Based on Your Budget")

if "search_params" not in st.session_state:
    st.error("Please go to the Home page and enter your trip details.")
    st.stop()

params = st.session_state.search_params

results = get_recommendations(params["location"], params["days"], params["budget"])

if results is None:
    st.warning("No matching trips found under the given budget.")
    st.stop()

geolocator = Nominatim(user_agent="trekonomix")
kolkata = (22.5726, 88.3639)

for i, trip in enumerate(results, 1):
    st.subheader(f"Option {i}: {trip['location']}")
    st.write(f"Trip Duration: {params['days']} days")
    st.write(f"Number of Persons: {trip['no_of_persons']}")
    st.write(f"Travel Purpose: {trip['travel_purpose']}")
    st.write(f"Accommodation Type: {trip['accommodation_type']}")
    st.write(f"Mode of Transport: {trip['mode_of_transport']}")

    on_budget = trip['total_budget_on_season_INR']
    off_budget = trip['total_budget_off_season_INR']

    st.write(f"Total Budget (On-season): ₹{on_budget}")
    st.write(f"Total Budget (Off-season): ₹{off_budget}")

    if off_budget < on_budget:
        st.success("Recommended Time: Off-season (More budget-friendly)")
    else:
        st.warning("Recommended Time: On-season (Better experience)")

    diff = abs(on_budget - off_budget)
    if diff >= 3000:
        st.info(f"Estimated Savings: ₹{diff} if you choose the cheaper season")

    st.info(f"Travel Tip: {get_travel_tip(trip['location'])}")

    dest = geolocator.geocode(trip["location"])
    if dest:
        dest_coords = (dest.latitude, dest.longitude)
    else:
        dest_coords = (20.5937, 78.9629)

    map_center = [(kolkata[0] + dest_coords[0]) / 2, (kolkata[1] + dest_coords[1]) / 2]
    m = folium.Map(location=map_center, zoom_start=5)
    folium.Marker(kolkata, tooltip="Kolkata", icon=folium.Icon(color="blue")).add_to(m)
    folium.Marker(dest_coords, tooltip=trip["location"], icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine([kolkata, dest_coords], color="green").add_to(m)
    st_folium(m, height=400, width=700)

    st.markdown("---")
