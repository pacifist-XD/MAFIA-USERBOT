# this plugin made by Mafia Userbot

"""Plugin for HellBot Repo

\nCode by @H1M4N5HU0P

type '.hellbot' to get HellBot repo
"""

import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="sorry ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://github.com/HellBoy-OP/HellBot) to open this 🔥**Lit AF!!**🔥 **Hêllẞø†** Repo.. Join channel :- @HellBot_Official Repo Uploaded By [𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)")
