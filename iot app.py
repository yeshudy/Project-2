from Adafruit_IO import Client
from telegram.ext import Updater, MessageHandler, Filters

consumer_name=os.getenv('consumer_name')
consumer_key=os.getenv('consumer_key')
bot_id=os.getenv('bot_id')

aio = Client('consumer_name','consumer_key')

def demo1(bot,update):
  aio.send('bedroom-light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turning on')

def demo2(bot,update):
  aio.send('bedroom-light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turning off')

def demo3(bot,update):
  aio.send('bedroom-fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turning on')

def demo4(bot,update):
  aio.send('bedroom-fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan is turning off')


def main(bot,update):
  a= bot.message.text.lower()
  if a =="Turn on light":
    demo1(bot,update)
  elif a =="Turn off light":
    demo2(bot,update) 
  elif a =="Turn on fan":
    demo3(bot,update)
  elif a =="Turn off fan":
    demo4(bot,update)      


bot_token ='bot_id'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
