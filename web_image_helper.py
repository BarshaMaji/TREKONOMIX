import requests

def fetch_web_image(query):
    try:
        url = f"https://source.unsplash.com/800x600/?{query}"
        return url
    except:
        return "https://source.unsplash.com/800x600/?travel"
