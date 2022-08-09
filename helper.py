from pyrogram import Client
from pyrogram.types import Message

async def get_id(_: Client, m: Message):
    if m.reply_to_message:
        try:
            id = m.reply_to_message.from_user.id
            r = None 
        except:
            id = None
            r = "User is with channel or with anonymous rights !"
    elif (not m.reply_to_message and len(m.command) > 1):
        text = m.text.split(None, 1)[1]
        if text[0] == "@":
            try:
                id = (await _.get_users(text)).id
                r = None
            except:
                id = None
                r = "Give username or id !"
        elif text.isnumeric():
            id = int(text)
            r = None
        else:
            id = None
            r = "Give username or id !"
    else:
        id = None 
        r = "/mute | /unmute @----- | id "

    return id, r
