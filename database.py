import json
import os

FILE = "last.json"


def load_last_link():
    try:
        if not os.path.exists(FILE):
            return None

        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("link")

    except:
        return None


def save_last_link(link):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump({"link": link}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("❌ خطا در ذخیره لینک:", e)