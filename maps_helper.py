from geopy.geocoders import Nominatim
import folium

def generate_map(destination):
    geolocator = Nominatim(user_agent="trekonomix_app")
    location = geolocator.geocode(destination)
    
    if location:
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)
        folium.Marker([location.latitude, location.longitude], tooltip=destination).add_to(m)
    else:
        m = folium.Map(location=[20.5937, 78.9629], zoom_start=4)  # Default: India
        folium.Marker([20.5937, 78.9629], tooltip="Unknown Location").add_to(m)

    return m
