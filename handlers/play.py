from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues
import asyncio

import converter
from downloaders import youtube
from asyncio.queues import QueueEmpty

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

aiohttpsession = aiohttp.ClientSession()
chat_id = None
DISABLED_GROUPS = []
useer ="NaN"


def cb_admin_check(func: Callable) -> Callable:
    async def decorator(client, cb):
        admemes = a.get(cb.message.chat.id)
        if cb.from_user.id in admemes:
            return await func(client, cb)
        else:
            await cb.answer("Bunu yapmana izin verilmiyor.!", show_alert=True)
            return
    return decorator 

@Client.on_message(command("oynat") & other_filters)
@errors
async def oynat(_, message: Message):

    lel = await message.reply("🔄 **ꜱᴇꜱʟᴇʀ ɪꜱʟᴇɴɪʏᴏʀ..**🔥")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🌀 Asistan",
                        url=f"https://t.me/musicbotasist"),
                    InlineKeyboardButton(
                        text="📣 Kanal​",
                        url=f"https://t.me/SohbetEmpire")
                 ],
                 [
                    InlineKeyboardButton(
                        text="🇹🇷 Creator 🇹🇷",
                        url=f"https://t.me/jackdanielssx"),
                    InlineKeyboardButton(
                        text="🇹🇷 Creator 🇹🇷",
                        url=f"https://t.me/mahoaga")
                  ],
                 [
                    InlineKeyboardButton(
                        text="🇹🇷 Botun Sahibi 🇹🇷",
                        url=f"https://t.me/Moriyonis")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)
    
@Client.on_message(command(["playlist"]) & filters.group & ~filters.edited)
async def playlist(client, message):
    global que
    if message.chat.id in DISABLED_GROUPS:
        return
    queue = que.get(message.chat.id)
    if not queue:
        await message.reply_text("**Akışta hiçbir şey yok!**")
    temp = []
    for t in queue:
        temp.append(t)
    now_playing = temp[0][0]
    by = temp[0][1].mention(style="md")
    msg = "**Çalınan Şarkılar** di {}".format(message.chat.title)
    msg += "\n• "+ now_playing
    msg += "\n• İstek üzerine "+by
    temp.pop(0)
    if temp:
        msg += "\n\n"
        msg += "**Şarkı Sırası**"
        for song in temp:
            name = song[0]
            usr = song[1].mention(style="md")
            msg += f"\n• {name}"
            msg += f"\n• Atas permintaan {usr}\n"
    await message.reply_text(msg)
    
# ============================= Settings =========================================
def updated_stats(chat, queue, vol=100):
    if chat.id in callsmusic.pytgcalls.active_calls:
        stats = "Ayarlar **{}**".format(chat.title)
        if len(que) > 0:
            stats += "\n\n"
            stats += "Ses: {}%\n".format(vol)
            stats += "Sırada şarkılar: `{}`\n".format(len(que))
            stats += "Şarkı çalma: **{}**\n".format(queue[0][0])
            stats += "İstek üzerine: {}".format(queue[0][1].mention)
    else:
        stats = None
    return stats

def r_ply(type_):
    if type_ == "oynat":
        pass
    else:
        pass
    mar = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⏹", "son"),
                InlineKeyboardButton("⏸", "durdur"),
                InlineKeyboardButton("▶️", "devam"),
                InlineKeyboardButton("⏭", "atla")
            ],
            [
                InlineKeyboardButton("📖 Şarkı bilgisi", "playlist"),
            ],
            [       
                InlineKeyboardButton("❎ Kapat", "cls")
            ]        
        ]
    )
    return mar
    
@Client.on_callback_query(filters.regex(pattern=r"^(playlist)$"))
async def p_cb(b, cb):
    global que    
    que.get(cb.message.chat.id)
    type_ = cb.matches[0].group(1)
    cb.message.chat.id
    cb.message.chat
    cb.message.reply_markup.inline_keyboard[1][0].callback_data
    if type_ == "playlist":
        queue = que.get(cb.message.chat.id)
        if not queue:
            await cb.message.edit("**Hiçbir şey oynamıyor.❗**")
        temp = []
        for t in queue:
            temp.append(t)
        now_playing = temp[0][0]
        by = temp[0][1].mention(style="md")
        msg = "**Şimdi yürütülen** in {}".format(cb.message.chat.title)
        msg += "\n• " + now_playing
        msg += "\n• Tarafından " + by
        temp.pop(0)
        if temp:
            msg += "\n\n"
            msg += "**Şarkı Sırası**"
            for song in temp:
                name = song[0]
                usr = song[1].mention(style="md")
                msg += f"\n• {name}"
                msg += f"\n• Req by {usr}\n"
        await cb.message.edit(msg)      

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("🤷‍♀️ ʙᴀɴᴀ ᴏʏɴᴀᴛɪʟᴀᴄᴀᴋ ᴍᴘ3 ꜰᴏʀᴍᴀᴛɪ ᴠᴇʀᴍᴇᴅɪɴ.!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="https://i.ibb.co/Qkz78hx/images-1.jpg",
        caption="**👤 ᴛᴀʟᴇᴘ ᴇᴅᴇɴ:** {}\n\n**#⃣ ꜱɪʀᴀᴅᴀᴋɪ ᴘᴀʀᴄᴀ ᴇᴋʟᴇɴᴅɪ:** {}".format( 
        message.from_user.mention(), position
        ),
        reply_markup=keyboard)
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="https://i.ibb.co/nwHdB2D/images.jpg",
        reply_markup=keyboard,
        caption="▶️ **ᴏʏɴᴀᴛɪʟɪʏᴏʀ** ʙᴜʀᴀᴅᴀ ɪꜱᴛᴇɴᴇɴ ꜱᴀʀᴋɪ ᴛᴀʀᴀꜰɪɴᴅᴀɴɪᴢᴅᴀɴ {}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
