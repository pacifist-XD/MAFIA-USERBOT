"""Fun pligon...for HardcoreUserbot

\nCode by @Kraken_The_BadASS

type `.ilu` to see the fun.
"""
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ilu ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "╔══╗╔╗╔═╦╗─╔╦═╗╔═╦╦═╦╦╗\n╚║║╝║║║║║╚╦╝║╦╝╚╗║║║║║║\n╔║║╗║╚╣║╠╗║╔╣╩╗╔╩╗║║║║║\n╚══╝╚═╩═╝╚═╝╚═╝╚══╩═╩═╝"
        )
