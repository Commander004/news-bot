import time

from rss import get_latest_news
from parser import parse_news
from database import load_last_link, save_last_link
from sender import send_news
from config import CHECK_INTERVAL

print("🟢 ربات خبری شروع شد...")

while True:

    try:
        news = get_latest_news()

        if not news:
            print("❌ خبری پیدا نشد")
            time.sleep(CHECK_INTERVAL)
            continue

        last_link = load_last_link()

        print("LAST:", last_link)
        print("NEW :", news["link"])

        # 🟢 جلوگیری از تکرار
        if news["link"] != last_link:

            print("🆕 خبر جدید پیدا شد")

            full_news = parse_news(news["link"])

            send_news(full_news)

            save_last_link(news["link"])

            print("💾 خبر ذخیره شد")

        else:
            print("ℹ️ خبر تکراری بود، رد شد")

    except Exception as e:
        print("❌ خطا:", e)

    time.sleep(CHECK_INTERVAL)