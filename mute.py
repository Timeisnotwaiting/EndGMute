from pyrogram import Client, filters
from pyrogram.types import Message
from config import *
from helper import get_id

alpha = Client(":Alpha:", API_ID, API_HASH, BOT_TOKEN)

@alpha.on_message(filters.command(["gmute", "ungmute"]) & ~filters.edited)
async def gmute(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
    id, r = await get_id(_, m)
    if not id:
        return await m.reply(r)
    muted = await is_muted(id)
    if not muted:
        ok = await m.reply("muting user.... ")
        try:
            await mute_user(id)
            await ok.edit(f"{(await _.get_users(id)).mention} gmuted !")
        except Exception as e:
            await ok.edit(f"can't add user id to database...\n\nError :- {e}")
    else:
        await m.reply("This user is already gmuted.... !")
    
    
