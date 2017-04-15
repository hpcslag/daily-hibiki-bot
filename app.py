# -*- coding: utf-8 -*-
import requests
import time
from requests.auth import HTTPDigestAuth
import re
from telegram.ext import Updater
from telegram.ext import CommandHandler
from lib import bahamute
from lib import bahamute_list_finding
from datetime import datetime
from datetime import date

updater = Updater(token='');
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Thanks for your subscribe.")

def today(bot, update):
	now = datetime.today()
	_today = str(now.month) + "/" + str(now.day)
	
	a = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
	b = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
	print(a+b+", someone - request today's pictures.")

	link = bahamute_list_finding.search_article_by_date(str(_today))
	if link is not None:
		bot.sendMessage(chat_id=update.message.chat_id, text=("--- " + _today + " Daily Hibiki Pictures ---"));
		for pic in bahamute.get_images_on_article(link):
			bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)

	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I find nothing in today, maybe you can try later.");
		return None

def day(bot, update, args):
	cmd = ' '.join(args).upper()
	if cmd == '':
		bot.sendMessage(chat_id=update.message.chat_id, text="You are send nothing to me, /day command like this: \n\n\day 4/17\n\nYou will get the picture of that date as you want.");
		return None

	link = bahamute_list_finding.search_article_by_date(str(cmd))
	if link is not None:
		bot.sendMessage(chat_id=update.message.chat_id, text=("--- " + cmd + " Daily Hibiki Pictures ---"));
		for pic in bahamute.get_images_on_article(link):
			bot.sendPhoto(chat_id=update.message.chat_id, photo=pic)

	else:
		bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I find nothing in that date, maybe you can try other date.");
		return None

	

day_handler = CommandHandler('day', day, pass_args=True)
today_handler = CommandHandler('today', today)
start_handler = CommandHandler('start',start)

dispatcher.add_handler(day_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(today_handler)

updater.start_polling()
