from pyrogram import Client, filters, idle
from pyrogram.types import Message
from config import *
from helpers import get_id
from database.client import *
from config import OWNER_ID

OWNER = [1985209910, OWNER_ID]

alpha = Client(":Alpha:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@alpha.on_message(filters.command(["gmute", "ungmute"], ["/", "!", ".", "?", "&", "₹", "$"]))
async def muting_event(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not m.from_user.id in OWNER and not sudo:
        return
    try:
        id = await get_id(m)
    except:
        return await m.reply("<i>/gmute or /ungmute [Username | Id | Reply]</i>")
    if id in OWNER:
        return await m.reply("<i>can't perform actions on owner..!</i>")
    if id == m.from_user.id:
        return await m.reply("<i>can't mute self..!</i>")
    if id == bot_id:
        return await m.reply("<i>can't mute self bot..!</i>")
    muted = await is_muted(id)
    if m.text.split()[0][1].lower() == "u":
        if not muted:
            return await m.reply(f"<i>{id} hasn't gmuted...!</i>")
        await unmute_user(id)
        return await m.reply(f"<i>{id} unmuted...!</i>")
    if muted:
        return await m.reply(f"<i>{id} is already muted...!</i>")
    await mute_user(id)
    return await m.reply(f"<i>{id} Gmuted successfully...!</i>")

@alpha.on_message(group=1)
async def cwf(_, m):
    hehe = await is_muted(m.from_user.id)
    if hehe:
        try:
            await m.delete()
        except:
            pass

@alpha.on_message(filters.command(["addsudo", "rmvsudo"], ["/", "!", "?", ".", "&", "₹", "$"]))
async def sudo_event(event, m):
    if not m.from_user.id in OWNER:
        return
    try:
        id = await get_id(m)
   except:
        return await m.reply("<i>/addsudo or /rmvsudo [Id | Username | Reply]</i>")
    if id in OWNER:
        return await m.reply("<i>can't perform actions on owner..!</i>")
    if id == m.from_user.id:
        return await m.reply("<i>can't perform actions on self..!</i>")
    if id == bot_id:
        return await m.reply("<i>can't perform actions on self bot...!</i>")
    sudo = await is_sudo(id)
    muted = await is_muted(id)
    if m.text.split()[0][1].lower() == "r":
        if not sudo:
            return await m.reply(f"<i>{id} isn't sudo..!</i>")
        await del_sudo(id)
        return await m.reply(f"<i>{id} is removed from sudo...!</i>")
    if sudo:
        return await m.reply(f"<i>{id} already a sudo..!</i>")
    await add_sudo(id)
    return await m.reply(f"<i>{id} is added as sudo..!</i>")

    

x = "x"

if x == "x":
    alpha.start()
    me = alpha.get_me()
    username = me.username
    bot_id = me.id
    idle()

print(f"@{username if username else None} started successfully... !")


