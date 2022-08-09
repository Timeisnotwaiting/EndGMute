from pyrogram import Client, filters
from pyrogram.types import Message
from config import *

alpha = Client(":Alpha:", API_ID, API_HASH, BOT_TOKEN)

@alpha.on_message(filters.command("gmute") & ~filters.edited)
async def gmute(_, m):
    sudo = await is_sudo(m.from_user.id)
    if not sudo:
        return
