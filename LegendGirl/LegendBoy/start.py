from pyrogram.types import InlineKeyboardButton

async def start_cmd(Legend):
    x = await Legend.get_me()
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
