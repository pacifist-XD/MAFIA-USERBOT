# This plugin made by 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 owner @H1M4N5HU0P

"""Fun plugin

\nCode by @H1M4N5HU0P

type `.please` to see the fun.
"""
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="please ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "╔═══╦╗──╔═══╦═══╦═══╦═══╗\n║╔═╗║║──║╔══╣╔═╗║╔═╗║╔══╝\n║╚═╝║║──║╚══╣║─║║╚══╣╚══╗\n║╔══╣║─╔╣╔══╣╚═╝╠══╗║╔══╝\n║║──║╚═╝║╚══╣╔═╗║╚═╝║╚══╗\n╚╝──╚═══╩═══╩╝─╚╩═══╩═══╝"
        )
