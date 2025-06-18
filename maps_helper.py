from geopy.geocoders import Nominatim
import folium

geolocator = Nominatim(user_agent="trekonomix")

def generate_map(destination):
    try:
        location = geolocator.geocode(destination)
        if location:
            lat, lon = location.latitude, location.longitude
        else:
            lat, lon = 20.5937, 78.9629  # Fallback to India
    except Exception as e:
        lat, lon = 20.5937, 78.9629

    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], tooltip=destination).add_to(m)
    return m
