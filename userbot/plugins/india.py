import asyncio

from mafiabot import *
from mafiabot.utils import *



@bot.on(admin_cmd(pattern=f"hrd$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hrd$", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
    

❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️🇮🇳❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
      

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
       

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
      

❤️❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
"""
)
        await event.edit("""
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
    

🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🇮🇳🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
      

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
       

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
      

🧡🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
"""
)

        await event.edit("""
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
    

💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳💛💛🇮🇳💛💛
💛💛🇮🇳💛🇮🇳💛🇮🇳💛💛
💛💛🇮🇳💛💛🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
      

💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
       

💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
      

💛💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
"""
)

        await event.edit("""
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
    

💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳💚💚🇮🇳💚💚
💚💚🇮🇳💚🇮🇳💚🇮🇳💚💚
💚💚🇮🇳💚💚🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
      

💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
       

💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
      

💚💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
"""
)

        await event.edit("""
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
    

💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳💙💙🇮🇳💙💙
💙💙🇮🇳💙🇮🇳💙🇮🇳💙💙
💙💙🇮🇳💙💙🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
      

💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
       

💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
      

💙💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
"""
)

        await event.edit("""
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
    

💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳💜💜🇮🇳💜💜
💜💜🇮🇳💜🇮🇳💜🇮🇳💜💜
💜💜🇮🇳💜💜🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
      

💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
       

💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
      

💜💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
"""
)

    
        await event.edit("""
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🇮🇳🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
"""
)

        await event.edit("""
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
    

❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️🇮🇳❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
      

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
       

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
      

❤️❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
"""
)
        await event.edit("""
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
    

🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🇮🇳🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
      

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
       

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
      

🧡🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
"""
)

        await event.edit("""
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
    

💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳💛💛🇮🇳💛💛
💛💛🇮🇳💛🇮🇳💛🇮🇳💛💛
💛💛🇮🇳💛💛🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
      

💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
       

💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
      

💛💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
"""
)

        await event.edit("""
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
    

💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳💚💚🇮🇳💚💚
💚💚🇮🇳💚🇮🇳💚🇮🇳💚💚
💚💚🇮🇳💚💚🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
      

💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
       

💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
      

💚💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
"""
)

        await event.edit("""
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
    

💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳💙💙🇮🇳💙💙
💙💙🇮🇳💙🇮🇳💙🇮🇳💙💙
💙💙🇮🇳💙💙🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
      

💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
       

💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
      

💙💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
"""
)

        await event.edit("""
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
    

💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳💜💜🇮🇳💜💜
💜💜🇮🇳💜🇮🇳💜🇮🇳💜💜
💜💜🇮🇳💜💜🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
      

💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
       

💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
      

💜💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
"""
)

    
        await event.edit("""
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🇮🇳🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
"""
)

        await event.edit("""
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
    

❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️🇮🇳❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
      

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
       

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
      

❤️❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
"""
)
        await event.edit("""
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
    

🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🇮🇳🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
      

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
       

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
      

🧡🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
"""
)

        await event.edit("""
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
    

💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳💛💛🇮🇳💛💛
💛💛🇮🇳💛🇮🇳💛🇮🇳💛💛
💛💛🇮🇳💛💛🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
      

💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
       

💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
      

💛💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
"""
)

        await event.edit("""
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
    

💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳💚💚🇮🇳💚💚
💚💚🇮🇳💚🇮🇳💚🇮🇳💚💚
💚💚🇮🇳💚💚🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
      

💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
       

💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
      

💚💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
"""
)

        await event.edit("""
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
    

💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳💙💙🇮🇳💙💙
💙💙🇮🇳💙🇮🇳💙🇮🇳💙💙
💙💙🇮🇳💙💙🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
      

💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
       

💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
      

💙💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
"""
)

        await event.edit("""
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
    

💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳💜💜🇮🇳💜💜
💜💜🇮🇳💜🇮🇳💜🇮🇳💜💜
💜💜🇮🇳💜💜🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
      

💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
       

💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
      

💜💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
"""
)

    
        await event.edit("""
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🇮🇳🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
"""
)

        await event.edit("""
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
    

❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️🇮🇳❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
      

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
       

❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️❤️❤️🇮🇳❤️❤️❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
      

❤️❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
❤️❤️🇮🇳❤️❤️❤️❤️🇮🇳❤️❤️
"""
)
        await event.edit("""
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
    

🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🇮🇳🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
      

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
       

🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🧡🧡🇮🇳🧡🧡🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
      

🧡🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
🧡🧡🇮🇳🧡🧡🧡🧡🇮🇳🧡🧡
"""
)

        await event.edit("""
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
    

💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳💛💛🇮🇳💛💛
💛💛🇮🇳💛🇮🇳💛🇮🇳💛💛
💛💛🇮🇳💛💛🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
      

💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
       

💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛💛💛🇮🇳💛💛💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
      

💛💛💛🇮🇳🇮🇳🇮🇳🇮🇳💛💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
💛💛🇮🇳💛💛💛💛🇮🇳💛💛
"""
)

        await event.edit("""
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
    

💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳💚💚🇮🇳💚💚
💚💚🇮🇳💚🇮🇳💚🇮🇳💚💚
💚💚🇮🇳💚💚🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
      

💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
       

💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚💚💚🇮🇳💚💚💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
      

💚💚💚🇮🇳🇮🇳🇮🇳🇮🇳💚💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
💚💚🇮🇳💚💚💚💚🇮🇳💚💚
"""
)

        await event.edit("""
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
    

💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳💙💙🇮🇳💙💙
💙💙🇮🇳💙🇮🇳💙🇮🇳💙💙
💙💙🇮🇳💙💙🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
      

💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
       

💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙💙💙🇮🇳💙💙💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
      

💙💙💙🇮🇳🇮🇳🇮🇳🇮🇳💙💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
💙💙🇮🇳💙💙💙💙🇮🇳💙💙
"""
)

        await event.edit("""
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
    

💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳💜💜🇮🇳💜💜
💜💜🇮🇳💜🇮🇳💜🇮🇳💜💜
💜💜🇮🇳💜💜🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
      

💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
       

💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜💜💜🇮🇳💜💜💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
      

💜💜💜🇮🇳🇮🇳🇮🇳🇮🇳💜💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
💜💜🇮🇳💜💜💜💜🇮🇳💜💜
"""
)

    
        await event.edit("""
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🇮🇳🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎


🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🤎🤎🇮🇳🤎🤎🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎


🤎🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
🤎🤎🇮🇳🤎🤎🤎🤎🇮🇳🤎🤎
"""
)
        await asyncio.sleep(2)
        await event.edit("🇮🇳**HAPPY REPUBLIC DAY TO YOU ALL🇮🇳**")
        
CmdHelp("india").add_command(
  "hrd", None, "Special Plugin For Republic Day")