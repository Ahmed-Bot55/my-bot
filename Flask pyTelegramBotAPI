import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "أهلاً يا أحمد! البوت شغال تمام ✅")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, f"استلمت: {m.text}")

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "البوت شغال!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
