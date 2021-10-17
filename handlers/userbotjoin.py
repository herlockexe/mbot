from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Önce beni yor grubunun yöneticisi olarak ekle</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "SerenityHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>sohbetinizde zaten yardımcı</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\nVeya grubunuza el ile ekleyin ve yeniden deneyin</b>",
        )
        return
    await message.reply_text(
            "<b>yardımcı userbot sohbetinize katıldı</b>",
        )
    
@USER.on_message(filters.group & filters.command(["asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı! Floodwaits olabilir."
            "\n\nYa da beni manuel olarak grubunuza tekmelersiniz.</b>",
        )
        return
