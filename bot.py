import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 

TOKEN = os.environ.get("TOKEN", "2035040893:AAF_cDCfMmq-rSlgedcG_IvafW5AiSXLe90")
API_ID = int(os.environ.get("API_ID", "6021226"))
API_HASH = os.environ.get("API_HASH", "7c6dd7679f9dc0ab599f336de13cedf1")

app = Client(
        "helper",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
    )

# Keep as Vars
START_TEXT = f"Hello There๐\n\n I Am SL Bot Zero Bot๐ฅฐ \nYou Can Contct SZ Admins And See our All Projects Using This Bot[โฆ](https://telegra.ph/file/89c42d6c34c89df58a5ef.jpg)"
START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ฑ Our Projects ๐ฑ", callback_data="botmenu")
                ],
                [
                    InlineKeyboardButton("๐ฎโโ๏ธ Owners ๐ฎโโ", url="https://t.me/sl_bot_zone"),
                    InlineKeyboardButton("๐ฐ Your Quizes ๐ฐ", url="https://t.me/sl_bot_zone")
                ],
                
                [
                    InlineKeyboardButton("๐ Our Website ๐", url="https://szbots.ml")
                ],
                [
                    InlineKeyboardButton("โ๏ธ Groupbโ๏ธ", url="https://t.me/slbotzone"),
                    InlineKeyboardButton("๐ฃ๏ธ Channal ๐ฃ๏ธ", url="https://t.me/szteambots")
                ]
            ]
        )

BOTS_TEXT = f"""
**Here There Welcome To Bot Menu๐คฉ\nThis Is A Our Bots And Projects ๐๐**
"""
BOTS_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Kingster Bot", callback_data="kingstermenu")
                ],
                [
                    InlineKeyboardButton("Go Back ๐", callback_data="startmenu")
                ]
            ]
        )

KINGSTER_TXT = f"""
๐คฉ Kingster Bot ๐คฉ

๐ฐ Kingster Is A Powerfull Telegram Group Manager Bot From Cool Moduals.. Kingster Has A Acribute Theme ๐ ๐คฉ Add Your Group And Enjoi ๐คฉ๐คฉ
"""

KINGSTER_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ Go To The Bot ๐", url="t.me/szkingster_bot")
                ]
            ]
        )
    
@app.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply_text(
        text=START_TEXT,
        disable_web_page_preview=False,
        reply_markup=START_BTN)   
    
@app.on_message(filters.command(["bots"]))
async def start(client, message):
    await message.reply_text(
        text=BOTS_TEXT,
        disable_web_page_preview=False,
        reply_markup=BOTS_BTN)     
    
@app.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=False
    )
    
@app.on_callback_query(filters.regex("botmenu"))
async def botsmenu(_, query: CallbackQuery):
    await query.edit_message_text(BOTS_TEXT,
        reply_markup=BOTS_BTN,
     disable_web_page_preview=False
    ) 

@app.on_message(filters.command(["kingster"]))
async def start(client, message):
    await message.reply_text(
        text=KINGSTER_TEXT,
        disable_web_page_preview=False,
        reply_markup=KINGSTER_BTN) 

@app.on_callback_query(filters.regex("kingstermenu"))
async def botsmenu(_, query: CallbackQuery):
    await query.edit_message_text(KINGSTER_TEXT,
        reply_markup=KINGSTER_BTN,
     disable_web_page_preview=False
    ) 
        
app.run()
