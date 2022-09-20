from pyrogram.types import Message
from database.client import get_flood_mode, set_flood_mode

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
    mode = get_flood_mode(m.chat.id)
    if mode == 1:
        return await _.ban_chat_member(m.chat.id, id)
    elif mode == 2:
        return await _.restriction_chat_member(m.chat.id, id, ChatPermissions())

    
