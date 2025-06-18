import requests
from bs4 import BeautifulSoup

def fetch_web_images(destination, max_images=3):
    search_url = f"https://duckduckgo.com/?q={destination}+travel+destination&iax=images&ia=images"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    image_urls = []

    for img_tag in soup.find_all("img"):
        src = img_tag.get("src")
        if src and "data:image" not in src and src.startswith("http"):
            image_urls.append(src)
        if len(image_urls) >= max_images:
            break

    return image_urls
