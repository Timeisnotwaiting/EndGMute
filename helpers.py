from pyrogram.types import Message, ChatPermissions
from database.client import get_flood_mode, set_flood_mode, set_flood
from pyrogram import Client
from mongo.flood import set_flood, get_flood
from PIL import Image, ImageFont, ImageDraw
import os

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
    mode = 1
    try:
        if mode == 1:
            return await _.ban_chat_member(m.chat.id, id)
    except Exception as e:
        return await m.reply(e)
    if mode == 2:
        return await _.restriction_chat_member(m.chat.id, id, ChatPermissions())

async def set_chat_flood(_, m):
    chat_id = m.chat.id
    try:
        value = int(m.text.split()[1])
    except Exception as e:
        return await m.reply(f"<i>/setflood < value ></i>")
    try:
        await set_flood(chat_id, value)
    except Exception as e:
        return await m.reply(e)
    return await m.reply(f"<i>flood value set to {value}</i>")

async def current_flood(_, m):
    x = await get_flood(m.chat.id)
    return await m.reply(f"{x}")

async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    shadowcolor = "black"
    i_width, i_height = img.size
    fnt = "ariel.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(image_name)
    img.save(webp_file, "webp")
    return webp_file

async def memify_event(_, m):
    if not m.reply_to_message:
        return await m.reply(m, f"<i>reply to a sticker..!</i>")
    if not m.reply_to_message.sticker:
        return await m.reply(m, f"<i>reply to a sticker..!</i>")
    if len(m.command) == 1:
        return await m.reply(m, f"<i>give some text to memify..!</i>")
    await m.reply(m, f"<i>memefying..!</i>")
    text = str(m.text.split(None, 1)[1])
    file = await _.download_media(m.reply_to_message, file_name=f"{m.from_user.id}.jpg")
    file_path = f"downloads/{m.from_user.id}.jpg"
    final = await drawText(file_path, text)
    await m.delete()
    await _.send_sticker(m.chat.id, final)
    os.remove(final)
    return 

    
