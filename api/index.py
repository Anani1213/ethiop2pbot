import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN", "8922741286:AAHHHDeVMNbmh-9RWG0hjY-Uza2Gxp0dRzo")

# ሁሉንም ሊመጡ የሚችሉ የ Route ጥሪዎችን እንዲቀበል አድርገነዋል
@app.route('/', methods=['GET', 'POST'])
@app.route('/api/index', methods=['GET', 'POST'])
@app.route('/api/index.py', methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def webhook(path=""):
    if request.method == 'GET':
        return "Ethio P2P Bot is running correctly!", 200

    try:
        data = request.get_json(force=True)
        
        if data and "message" in data:
            message = data["message"]
            chat_id = message["chat"]["id"]
            first_name = message["from"].get("first_name", "")
            text = message.get("text", "")

            if text.startswith("/start"):
                reply_text = f"hi {first_name} wellcome to ethio p2p click open p2p and start exchange"
                
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
