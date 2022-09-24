from pyrogram.types import Message, ChatPermissions
from database.client import get_flood_mode, set_flood_mode, set_flood
from pyrogram import Client

async def get_id(m: Message):
    if not m.reply_to_message:
        text = m.text.split()
        un_or_id = text[1]
        if un_or_id[0] == "@":
            id = (await _.get_users(un_or_id)).id
        else:
            id = int(un_or_id)
    else:
        id = m.reply_to_message.from_user.id
    return id 

async def do_action(_: Client, m: Message, id):
    try:
        mode = get_flood_mode(m.chat.id)
    except:
        mode = 1
    if mode == 1:
        return await _.ban_chat_member(m.chat.id, id)
    elif mode == 2:
        return await _.restriction_chat_member(m.chat.id, id, ChatPermissions())

async def set_chat_flood(_, m):
    chat_id = m.chat.id
    try:
        value = int(m.text.split()[1])
    except Exception as e:
        return await m.reply(f"<i>/setflood < value ></i>")
    try:
        set_flood(chat_id, value)
    except Exception as e:
        return await m.reply(e)
    return await m.reply(f"<i>flood value set to {value}</i>")


    
    
