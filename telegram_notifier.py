#!/usr/bin/python3
import settings
import telebot
import os

if os.path.exists(settings.FLAG_FILE_PATH):
    bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
    bot.send_message(settings.CHAT_ID, settings.ALARM_MESSAGE)
