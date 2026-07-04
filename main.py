import time
import random

from config import NEWS_SOURCES
from rss import get_latest_news
from sender import send_news


print("🟢 ربات خبری شروع شد...")

last_sent = None  # برای جلوگیری از تکرار

while True:
    try:

        # 🎲 انتخاب رندوم از بین سایت‌ها
        source = random.choice(NEWS_SOURCES)
        print("📡 منبع انتخاب شده:", source)

        # 📰 گرفتن خبر از همون سایت
        news = get_latest_news(source)

        # ❌ اگر خبری نبود
        if not news:
            print("⚠️ خبری پیدا نشد")
            time.sleep(20)
            continue

        print("NEW:", news["link"])

        # 🔁 جلوگیری از ارسال خبر تکراری
        if news["link"] == last_sent:
            print("🔁 خبر تکراری بود، رد شد")
            time.sleep(20)
            continue

        print("🆕 خبر جدید پیدا شد")

        # 📤 ارسال به کانال
        send_news(news)

        # 💾 ذخیره آخرین خبر
        last_sent = news["link"]

        # ⏱ مکث برای جلوگیری از فشار به سایت
        time.sleep(100)

    except Exception as e:
        print("❌ خطا:", e)
        time.sleep(120)
