import os
from flask import Flask, request
import telebot

# ከ Vercel Environment Variables ላይ BOT_TOKEN ይወስዳል
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# ተጠቃሚው /start ሲል የሚላክ መልእክት
@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    text = f"hi {name} wellcome to ethio p2p click open p2p and start exchange"
    bot.reply_to(message, text)

# ለ Vercel Serverless የሚሆን Webhook መንገድ
@app.route('/api/index', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Forbidden', 403

@app.route('/', methods=['GET'])
def home():
    return "Bot is running on Vercel!"
