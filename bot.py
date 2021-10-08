import os
import requests as re
from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

TOKEN = os.environ.get("TOKEN", "2035040893:AAF_cDCfMmq-rSlgedcG_IvafW5AiSXLe90")

API_ID = int(os.environ.get("API_ID", "6021226"))

API_HASH = os.environ.get("API_HASH", "7c6dd7679f9dc0ab599f336de13cedf1")

app = Client(
        "webscrap",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )
    
    
@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n I Am SL Bot Zero Bot🥰 \nYou Can Contct SZ Admins And See our All Projects Using This Bot[…](https://t.me/omindas)",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔱 Our Projects 🔱" ,callback_data="bots") ],
                    
[InlineKeyboardButton("🌐 Our Website 🌐" ,url="https://szbots.ml") ],

[InlineKeyboardButton("👮‍♂️ Owners 👮‍♂️" ,url="https://t.me/slbotzone"),
InlineKeyboardButton("🔰 Ask 🔰" ,url="https://t.me/sl_bot_zone") ],

[InlineKeyboardButton("✍️ Groupb✍️" ,url="https://t.me/slbotzone"),
InlineKeyboardButton("🗣️ Channal 🗣️" ,url="https://t.me/sl_bot_zone") ],
              
                 [InlineKeyboardButton("🚀 YouTube 🚀", url="https://youtube.com/c/SlGeekShow") ]          ]        ) )


@app.on_message(filters.command(['bots']))
def start(client, message):
            message.reply_text(text  =f"Welcome To Bots Menu 🔰\n\nYou Can See A Our Bots Frome This Button Menu\nClick In A Bot Name Butto And See A Bots Info 🗣️",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔱 Our Projects 🔱" ,url="https://t.me/slbotzone") ],
                    
[InlineKeyboardButton("🌐 Our Website 🌐" ,url="https://szbots.ml") ],

[InlineKeyboardButton("👮‍♂️ Owners 👮‍♂️" ,url="https://t.me/slbotzone"),
InlineKeyboardButton("🔰 Ask 🔰" ,url="https://t.me/sl_bot_zone") ],

[InlineKeyboardButton("✍️ Groupb✍️" ,url="https://t.me/slbotzone"),
InlineKeyboardButton("🗣️ Channal 🗣️" ,url="https://t.me/sl_bot_zone") ],
              
                 [InlineKeyboardButton("🚀 YouTube 🚀", url="https://youtube.com/c/SlGeekShow") ]          ]        ) )

        
app.run()
