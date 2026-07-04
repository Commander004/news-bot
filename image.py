import requests
from bs4 import BeautifulSoup


def get_image(url):

    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        img = soup.find("meta", property="og:image")

        if img:
            return img["content"]

    except:
        pass

    return None
