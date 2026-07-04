# parser.py

import requests
from bs4 import BeautifulSoup


def parse_news(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(html, "html.parser")
    # عنوان
    title_tag = soup.find(class_="title_news")
    title = title_tag.get_text(" ", strip=True) if title_tag else ""

    # زیرتیتر
    sub_tag = soup.find(class_="subtitle")
    subtitle = sub_tag.get_text(" ", strip=True) if sub_tag else ""

    # متن
    body_tag = soup.find(class_="news_center_body") or soup.find(class_="news_top_body")
    body = body_tag.get_text("\n", strip=True) if body_tag else ""

    # عکس
    image = None
    for img in soup.find_all("img"):
        src = img.get("src")
        if src and "/files/" in src:
            image = "https://www.iribnews.ir" + src if src.startswith("/") else src
            break

    return {
        "title": title,
        "subtitle": subtitle,
        "body": body,
        "image": image,
        "link": url
    }
