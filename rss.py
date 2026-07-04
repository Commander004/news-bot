import feedparser


def get_latest_news(source):
    feed = feedparser.parse(source)

    if not feed.entries:
        return None

    entry = feed.entries[0]

    # 🟢 عکس
    image = None

    if hasattr(entry, "media_content"):
        image = entry.media_content[0].get("url")

    elif hasattr(entry, "media_thumbnail"):
        image = entry.media_thumbnail[0].get("url")

    # 🟢 خروجی تمیز
    return {
        "title": entry.title,
        "subtitle": entry.get("summary", ""),
        "body": entry.get("summary", ""),
        "link": entry.link,
        "image": image
    }
