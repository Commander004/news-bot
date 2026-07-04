# rss.py

import feedparser
from config import RSS_URL


def get_latest_news():
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return None

    latest = feed.entries[0]

    return {
        "title": latest.title,
        "link": latest.link
    }	