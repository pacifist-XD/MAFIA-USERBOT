import asyncio

from telethon.tl.types import MessageEntityMentionName
from uniborg.util import admin_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Something Went Wrong", str(err))
    return user_obj, extra


@borg.on(admin_cmd(pattern="insult", outgoing=True))
async def _(event):
    await event.edit("[{user_obj}](tg://user?id={user_id}) dont drink and type.")
    await asyncio.sleep(2)
    await event.edit(
        "I think [{user_obj}](tg://user?id={user_id}) should go home or better, a mental asylum."
    )
    await asyncio.sleep(2)
    await event.edit(
        "Command not found. Just like [{user_obj}](tg://user?id={user_id}) brain."
    )
    await asyncio.sleep(2)
    await event.edit(
        "[{user_obj}](tg://user?id={user_id}) do you realize you are making a fool of yourself? Apparently not."
    )
    await asyncio.sleep(2)
    await event.edit(
        "[{user_obj}](tg://user?id={user_id}), you can type better than that."
    )
    await asyncio.sleep(2)
    await event.edit(
        "Bot rule 544 section 9 prevents me from replying to stupid humans like [{user_obj}](tg://user?id={user_id})."
    )
    await asyncio.sleep(2)
    await event.edit(
        "[{user_obj}](tg://user?id={user_id}) sorry, we do not sell brains."
    )
