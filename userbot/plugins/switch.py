"""Emoji

Available Commands:

.switch"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "switch":

        await event.edit(input_str)

        animation_chars = [
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n[👉](https://t.me/H1M4N5HU0P)⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬛[👉](https://t.me/H1M4N5HU0P)⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬜⬜⬜⬜⬜⬜\n⬜[👆](https://t.me/H1M4N5HU0P)⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜[👆](https://t.me/H1M4N5HU0P)⬜⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬛[👉](https://t.me/H1M4N5HU0P)⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/H1M4N5HU0P/MAFIA-USERBOT)\n⬜⬛⬛[👉](https://t.me/H1M4N5HU0P)⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🔲\n⬜⬛⬛⬛[👉](https://t.me/H1M4N5HU0P)⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜[👆](https://t.me/H1M4N5HU0P)⬜🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬛[👉](https://t.me/H1M4N5HU0P)🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🔳\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
