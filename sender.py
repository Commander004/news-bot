import requests
from config import BOT_TOKEN, CHANNEL_ID


def send_news(news):

    print("📤 در حال ارسال پیام...")

    caption = f"""
📰 {news['title']}

📝 {news['subtitle']}

━━━━━━━━━━━━━━
📢 @AkhbarLahzaei_ir
"""

    try:

        # 🟢 اگر عکس داشت
        if news.get("image"):

            url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendPhoto"

            data = {
                "chat_id": CHANNEL_ID,
                "photo": news["image"],
                "caption": caption
            }

        else:

            url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"

            data = {
                "chat_id": CHANNEL_ID,
                "text": caption
            }

        r = requests.post(url, data=data)

        print("📨 پاسخ:", r.text)
        print("✅ خبر ارسال شد")

    except Exception as e:
        print("❌ خطا:", e)
