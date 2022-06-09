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
        caption=f"""**𝐓𝐇𝐈𝐒 𝐈𝐒 𝐁𝐄𝐒𝐓 𝐐𝐔𝐀𝐋𝐈𝐓𝐘 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 𝐑𝐔𝐍𝐍𝐈𝐍𝐆 𝐎𝐍 𝐑𝐀𝐈𝐋𝐖𝐀𝐘 𝐒𝐄𝐑𝐕𝐄𝐑 = [💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔](https://t.me/ITZ_B_R_O_K_E_N)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔](https://t.me/ITZ_B_R_O_K_E_N)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [𝐂𝐇𝐀𝐓𝐓𝐈𝐍𝐆 ✍︎](https://t.me/The_Exterminators)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [𝐆𝐑𝐎𝐔𝐏 ✌︎](https://t.me/The_Exterminators)

𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 = [💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔](https://t.me/ITZ_B_R_O_K_E_N)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐉𝐨𝐢𝐧 𝐌𝐲 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/The_Exterminators")
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
                        "Rᴇᴘᴏ", url=f"https://t.me/The_Exterminators")
                ]
            ]
        ),
    )
