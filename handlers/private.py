import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/35c5ff1fc7559d30d8892.jpg",
        caption=f"""**ðððð ðð ðððð ððððððð ððððð ððð ððððððð ðð ððððððð ðððððð = [ðð ðððððð ðð](https://t.me/ITZ_B_R_O_K_E_N)

ðð«ððð­ð¨ð« :- [ðð ðððððð ðð](https://t.me/ITZ_B_R_O_K_E_N)
ðð®ð©ð©ð¨ð«ð­ :- [ðððððððð âï¸](https://t.me/The_Exterminators)
ðð¢ð¬ðð®ð¬ð¬ :- [ððððð âï¸](https://t.me/The_Exterminators)

ðð§ð² ðð«ð¨ðð¥ðð¦ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð°ð§ðð« = [ðð ðððððð ðð](https://t.me/ITZ_B_R_O_K_E_N)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ðð¨ð¢ð§ ðð² ðð¡ðð­ ðð«ð¨ð®ð©", url=f"https://t.me/The_Exterminators")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/35c5ff1fc7559d30d8892.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Rá´á´á´", url=f"https://t.me/The_Exterminators")
                ]
            ]
        ),
    )
