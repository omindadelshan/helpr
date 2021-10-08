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
START_TEXT = f"Hello There👋\n\n I Am SL Bot Zero Bot🥰 \nYou Can Contct SZ Admins And See our All Projects Using This Bot[…](https://telegra.ph/file/89c42d6c34c89df58a5ef.jpg)"
START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔱 Our Projects 🔱", callback_data="botmenu")
                ],
                [
                    InlineKeyboardButton("👮‍♂️ Owners 👮‍♂", url="https://t.me/sl_bot_zone"),
                    InlineKeyboardButton("🔰 Your Quizes 🔰", url="https://t.me/sl_bot_zone")
                ],
                
                [
                    InlineKeyboardButton("🌐 Our Website 🌐", url="https://szbots.ml")
                ],
                [
                    InlineKeyboardButton("✍️ Groupb✍️", url="https://t.me/slbotzone"),
                    InlineKeyboardButton("🗣️ Channal 🗣️", url="https://t.me/szteambots")
                ]
            ]
        )

BOTS_TEXT = f"""
**Here There Welcome To Bot Menu🤩\nThis Is A Our Bots And Projects 👇👇**
"""
BOTS_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Go Back 👈", callback_data="startmenu")
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
        
app.run()
