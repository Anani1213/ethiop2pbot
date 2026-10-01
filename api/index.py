import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name if message.from_user else ""
    text = f"hi {name} wellcome to ethio p2p click open p2p and start exchange"
    bot.reply_to(message, text)

# ማንኛውንም የ Vercel Route ለማስተናገድ
@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>', methods=['POST', 'GET'])
def main_handler(path):
    if request.method == 'POST':
        try:
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return 'OK', 200
        except Exception as e:
            return str(e), 500
    return "Bot is running on Vercel!", 200
