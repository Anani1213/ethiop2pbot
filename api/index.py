import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ከ Vercel Environment Variable ወይም ቀጥታ Token ይወስዳል
BOT_TOKEN = os.getenv("BOT_TOKEN", "8922741286:AAHHHDeVMNbmh-9RWG0hjY-Uza2Gxp0dRzo")

@app.route('/', methods=['GET'])
def home():
    return "Ethio P2P Bot is running!", 200

@app.route('/api/index', methods=['POST'])
@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        
        # ከቴሌግራም መልእክት ሲመጣ
        if data and "message" in data:
            message = data["message"]
            chat_id = message["chat"]["id"]
            first_name = message["from"].get("first_name", "")
            text = message.get("text", "")

            # /start ሲባል የሚላክ
            if text.startswith("/start"):
                reply_text = f"hi {first_name} wellcome to ethio p2p click open p2p and start exchange"
                
                # ቀጥታ ለቴሌግራም API መልእክቱን መላክ
                telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": chat_id,
                    "text": reply_text
                }
                requests.post(telegram_url, json=payload)

        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 200
