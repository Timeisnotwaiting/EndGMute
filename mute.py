from pyrogram import Client, filters, idle
from pyrogram.types import Message
from config import *
from helpers import get_id
from database.client import *
from config import OWNER_ID

FLOOD_ID = []

a = 0

OWNER = [1985209910, OWNER_ID]

alpha = Client(":Alpha:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@alpha.on_message(filters.command(["gmute", "ungmute"], ["/", "!", ".", "?", "&", "₹", "$"]))
async def muting_event(_, m):
    sudo = is_sudo(m.from_user.id)
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
    muted = is_muted(id)
    if m.text.split()[0][1].lower() == "u":
        if not muted:
            return await m.reply(f"<i>{id} hasn't gmuted...!</i>")
        unmute_user(id)
        return await m.reply(f"<i>{id} unmuted...!</i>")
    if muted:
        return await m.reply(f"<i>{id} is already muted...!</i>")
    mute_user(id)
    return await m.reply(f"<i>{id} Gmuted successfully...!</i>")

@alpha.on_message(group=1)
async def cwf(_, m):
    global FLOOD_ID, a
    hehe = is_muted(m.from_user.id)
    if hehe:
        try:
            await m.delete()
        except:
            pass
    if m.from_user:
        if flood_value != 0:
            if not FLOOD_ID:
                FLOOD_ID.append(m.from_user.id)
                a = 1
            else:
                if m.from_user.id in FLOOD_ID:
                    a += 1
                else:
                    FLOOD_ID.clear()
                    a = 0

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
    sudo = is_sudo(id)
    muted = is_muted(id)
    if m.text.split()[0][1].lower() == "r":
        if not sudo:
            return await m.reply(f"<i>{id} isn't sudo..!</i>")
        del_sudo(id)
        return await m.reply(f"<i>{id} is removed from sudo...!</i>")
    if sudo:
        return await m.reply(f"<i>{id} already a sudo..!</i>")
    unmute_user(id)
    add_sudo(id)
    return await m.reply(f"<i>{id} is added as sudo..!</i>")

@alpha.on_message(filters.command("sudos", ["/", "!", "?", ".", "&", "₹", "$"]))
async def get_event(_, m):
    sudo = is_sudo(m.from_user.id)
    if not m.from_user.id in OWNER and not sudo:
        return
    msg = ""
    sudos = get_sudos()
    for sudo in sudos:
        sudo = str(sudo)
        msg += f"<code>{sudo}</code>\n"
    if msg == "":
        return await m.reply("<i>Sudo List is empty..!</i>")
    return await m.reply(f"<i>Users :-</i>\n\n{msg}")
        

@alpha.on_message(filters.command("muted", ["/", "!", "?", ".", "&", "₹", "$"]))
async def get__event(_, m):
    muted = is_muted(m.from_user.id)
    if not m.from_user.id in OWNER and not sudo:
        return
    msg = ""
    sudos = get_muted()
    for sudo in sudos:
        sudo = str(sudo)
        msg += f"<code>{sudo}</code>\n"
    if msg == "":
        return await m.reply("<i>Muted List is empty..!</i>")
    return await m.reply(f"<i>Users :-</i>\n\n{msg}")

x = "x"

if x == "x":
    alpha.start()
    me = alpha.get_me()
    username = me.username
    bot_id = me.id
    print(f"@{username if username else None} started successfully... !")
    idle()



