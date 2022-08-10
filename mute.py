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
    sudo_check = await is_sudo(id)
    if sudo_check:
        return await m.reply("Can't gmute sudo users.... !")
    muted = await is_muted(id)
    if m.text.split()[0][1].lower() == "u":
        if muted:
            ok = await m.reply("unmuting user.... ")
            try:
                await unmute_user(id)
                return await ok.edit(f"{(await _.get_users(id)).mention} unmuted !")
            except:
                return await ok.edit("Error at database !")
        else:
            return await m.reply("This user is not muted.... !")
    if not muted:
        ok = await m.reply("muting user.... ")
        try:
            await mute_user(id)
            return await ok.edit(f"{(await _.get_users(id)).mention} gmuted !")
        except Exception as e:
            return await ok.edit(f"can't add user id to database...\n\nError :- {e}")
    else:
        return await m.reply("This user is already gmuted.... !")
    
    
@alpha.on_message(group=1)
async def cwf(_, m):
    MUTED = await get_muted()
    if m.from_user.id in MUTED:
        try:
            return await m.delete()
        except:
            return 

@alpha.on_message(filters.command(["addsudo", "delsudo"])
