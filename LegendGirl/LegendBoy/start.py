from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Data import Data
from LegendGirl.Config import *

if START_OP:
    START_OP = START_OP
else:
    START_OP = [
        [
            InlineKeyboardButton(
                text="🥀 Developer 🥀", url=f"https://t.me/MR_AGORA"
            ),
            InlineKeyboardButton(
                text="✨ Support ✨", url=f"https://t.me/AGORAWORLD"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🧸 Add me in your group 🧸",
                url=f"https://t.me/Agoraxrobot?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❄️ Source Code ❄️", url=f"https://t.me/kimjikoin_bot?startgroup=true"
            ),
            InlineKeyboardButton(
                text="☁️ Updates ☁️", url=f"https://t.me/teamagora"
            ),
        ],
    ]
    return START_OP
