import os, telebot
from flask import Flask
from threading import Thread
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
@bot.message_handler(func=lambda m: True)
def echo(m): bot.reply_to(m, f"قلت: {m.text}")
app = Flask('')
@app.route('/')
def home(): return "alive"
Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))).start()
bot.infinity_polling()
