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
    if m.text.split()[0][1].lower == "u":
        if muted:
            ok = await m.reply("unmuting user.... ")
            try:
                await unmute_user(id)
                return await ok.edit(f"{(await _.get_users(id)).mention} unmuted !")
            except:
                return await ok.edit("Error at database !")
    if not muted:
        ok = await m.reply("muting user.... ")
        try:
            await mute_user(id)
            return await ok.edit(f"{(await _.get_users(id)).mention} gmuted !")
        except Exception as e:
            return await ok.edit(f"can't add user id to database...\n\nError :- {e}")
    else:
        await m.reply("This user is already gmuted.... !")
    
    
