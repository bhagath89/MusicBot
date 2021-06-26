from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CUJU0dgACAppgyWsRKZJ0W4hbRKdVMYuxwb50wwACgxcAAtqjlSw9sWir1m6CTx8E")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 I am JANAKI Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉


⚜️You can make your own music bot just tap on deploy link 🔱


Developed by @FlyingKILI


My commands - type  /help to get commands, which work in grp

Thanks for using .

Regrards [LEGEND](https://t.me/FlyingKILI)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "DEPLOY LINK", url="https://t.me/Uvvauvve")
                  ],[
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/FlyingKILI"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/FlyingKILI"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Janaki_musicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🌸JANAKI MUSIC PLAYER IS ALWAYS ACTIVE!!🌸**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/FlyingKILI")
                ]
            ]
        )
   )
