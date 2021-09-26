from Adafruit_IO import Client
from telegram.ext import Updater, MessageHandler, Filters
import os

consumer_name=os.getenv('consumer_name')
consumer_key=os.getenv('consumer_key')
bot_id=os.getenv('bot_id')

aio = Client('consumer_name','consumer_key')

def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light is turning on')
  aio.send('bedroom-light',1)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light is turning off')
  aio.send('bedroom-light',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('fan is turning on')
  aio.send('bedroom-fan',1)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('fan is turning off')
  aio.send('bedroom-fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on light":
    demo1(bot,update)
  elif a =="turn off light":
    demo2(bot,update)
  elif a =="turn on fan":
    demo3(bot,update)
  elif a =="turn off fan":
    demo4(bot,update)    

bot_token = '2008744403:AAHmmYcaJHza6ClHEhTGTb5Jlc7jroHWvjI'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
