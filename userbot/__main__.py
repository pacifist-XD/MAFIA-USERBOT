from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.utils import load_module
from userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("𝕐𝕆𝕌ℝ 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝕀𝕊 ℝ𝔼𝔸𝔻𝕐 𝕋𝕆 𝕌𝕊𝔼! 𝔽𝕆ℝ ℂℍ𝔼ℂ𝕂 𝕐𝕆𝕌ℝ 𝔹𝕆𝕋 𝕎𝕆ℝ𝕂𝕀ℕ𝔾 𝕆ℝ ℕ𝕆𝕋 ℙ𝕃𝔼𝔸𝕊𝔼 𝕋𝕐ℙ𝔼 (.alive/.mafia/.ping) 𝔼ℕ𝕁𝕆𝕐 𝕐𝕆𝕌ℝ 𝔹𝕆𝕋! 𝕁𝕆𝕀ℕ 𝔽𝕆ℝ 𝕄𝕆ℝ𝔼 𝔽𝕌𝕋𝕌ℝ𝔼 𝕌ℙ𝔻𝔸𝕋𝔼𝕊 @MAFIA_USERBOT ")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


