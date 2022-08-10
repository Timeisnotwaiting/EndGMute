from pyrogram import Client, filters
from pyrogram.types import Message
from config import *
from helper import get_id
from database.client import *


alpha = Client(":Alpha:", API_ID, API_HASH, BOT_TOKEN)

@alpha.on_message(filters.command(["gmute", "ungmute"]))
async def gmute(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
    id, r = await get_id(_, m)
    if not id:
        return await m.reply(r)
    if id == bot_id:
        return await m.reply("You can't mute self bot.... ")
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

@alpha.on_message(filters.command(["addsudo", "delsudo"]))
async def sudo(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
    id, r = await get_id(_, m)
    if not id:
        return await m.reply(r)
    if id == m.from_user.id:
        return await m.reply("You can't add / del self as sudo...")
    if id == bot_id:
        return await m.reply("You can't add self as sudo.... ")
    muted = await is_muted(id)
    sudo = await is_sudo(id)
    if is_sudo:
        if m.text.split()[0][1].lower() == "d":
            await del_sudo(id)
            return await m.reply("removed sudo ....")
    men = (await _.get_users(id)).mention
    if not sudo:
        await add_sudo(id)
        if muted:
            await unmute_user(id)
        return await m.reply(f"{men} is added as sudo.. !")
    return await m.reply("This user is already a sudo...")

@alpha.on_message(filters.command("sudos"))
async def get_s(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
    msg = ""
    SUDOS = await get_sudos()
    for sudos in SUDOS:
        sudos = str(sudos)
        msg += f"\n{sudos}"
    final = f"List of sudo :- \n{msg}"
    return await m.reply(final)
    

alpha.start()
me = alpha.get_me()
username = me.username
bot_id = me.id
print(f"@{username if username else None} started successfully... !")



