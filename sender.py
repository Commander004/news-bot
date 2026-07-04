import requests
from config import BOT_TOKEN, CHANNEL_ID
from image import get_image


def send_news(news):

    print("📤 در حال ارسال خبر...")

    photo = get_image(news["link"])

    if not photo:
        photo = "https://i.imgur.com/default.jpg"

    caption = f"""
📰 {news['title']}

📝 {news['subtitle']}

━━━━━━━━━━━━━━
📢 @AkhbarLahzaei_ir
"""

    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendPhoto"

    data = {
        "chat_id": CHANNEL_ID,
        "photo": photo,
        "caption": caption
    }

    r = requests.post(url, data=data)

    print("📨 پاسخ:", r.text)

    if r.status_code == 200:
        print("✅ خبر با عکس ارسال شد")
    else:
        print("❌ ارسال ناموفق")
