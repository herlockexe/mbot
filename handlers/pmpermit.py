from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba, Müzik asistanı hizmetidir.\n\n ❗️ Kurallar:\n   - Sohbete izin yok\n   - İstenmeyen postaya izin verilmez\n\n 👉 **USERBOT GRUBUNUZA KATILAMAZSA GRUP DAVET BAĞLANTISI VEYA KULLANICI ADI GÖNDER.**\n\n ⚠️ Disclamer: Burada bir mesaj gönderiyorsanız, yönetici mesajınızı görecek ve sohbete katılacaktır\n    - Bu kullanıcıyı gizli gruplara eklemeyiniz.\n   - Özel bilgileri burada paylaşmayın\n\n")
  return                        
