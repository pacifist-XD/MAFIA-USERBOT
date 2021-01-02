import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events	
@borg.on(admin_cmd(pattern="insult", outgoing=True))
async def _(event):
		await event.edit("[{}](tg://user?id={}) dont drink and type.")
		await asyncio.sleep(2)
		await event.edit("I think [{}](tg://user?id={}) should go home or better, a mental asylum.")
		await asyncio.sleep(2)
		await event.edit("Command not found. Just like [{}](tg://user?id={}) brain.")
		await asyncio.sleep(2)
		await event.edit("[{}](tg://user?id={}) do you realize you are making a fool of yourself? Apparently not.")
		await asyncio.sleep(2)
		await event.edit("[{}](tg://user?id={}), you can type better than that.")
		await asyncio.sleep(2)
		await event.edit("Bot rule 544 section 9 prevents me from replying to stupid humans like [{}](tg://user?id={}).")
		await asyncio.sleep(2)
		await event.edit("[{}](tg://user?id={}) sorry, we do not sell brains.")
		
		