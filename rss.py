import feedparser
import random
from config import NEWS_SOURCES


def get_latest_news():

    url = random.choice(NEWS_SOURCES)
    feed = feedparser.parse(url)

    if not feed.entries:
        return None

    latest = feed.entries[0]

    return {
        "title": latest.title,
        "subtitle": latest.get("summary", "بدون توضیح"),
        "link": latest.link
    }	
