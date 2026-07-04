import requests
from config import BOT_TOKEN, CHANNEL_ID


def send_news(news):

    print("📤 در حال ارسال پیام...")

    caption = f"""
📰 {news['title']}

📝 {news['subtitle']}

🔗 {news['link']}

━━━━━━━━━━━━━━
📢 @AkhbarLahzaei_ir
"""

    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_ID,
        "text": caption
    }

    try:
        r = requests.post(url, data=data)

        print("📨 پاسخ:", r.text)
        print("✅ خبر ارسال شد")

    except Exception as e:
        print("❌ خطا:", e)