from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""Merhaba 👋! **Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Sizi şaşırtacak pek çok harika özelliğim var!** 🥳 \n\n🔴 **Telegramda Beni nasıl kullanabileceğinizi öğrenmek için lütfen >> /help Butonuna basınız.** \n\n🔴 **Grubunuzun sesli sohbetinde, Müzik çalabilmem için Asistanın Grubunuzda olması gerekir.** \n\n🔵 Bu çalışma [Sohbet Destek](https://t.me/SohbetEmpire) Tarafından keyfe değer düzenlenmiştir.!
      """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📣 Resmi Kanal", url="https://t.me/jackmedya")
                  ],[
                    InlineKeyboardButton(
                        "💬 Sohbet Grubu", url="https://t.me/SohbetEmpire"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎵 Mp3 Arama Botu", url="https://t.me/DeezerMusicBot"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "🎯 Usertagger Bot", url="https://t.me/EmpireTaggerBot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️YouTube videosu aramak istiyor musunuz? ?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/SohbetEmpire"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.first_name}! 
\n/oynat - ᴍᴘ3 ꜰᴏʀᴍᴀᴛɪɴᴀ ᴜʏɢᴜɴ ᴅᴏꜱʏᴀʟᴀʀɪ ᴄᴀʟɪꜱᴛɪʀᴍᴀᴋ ɪᴄɪɴ ᴅᴇᴇꜱᴇʀ ᴍᴜꜱɪᴄ ᴅᴇꜱᴛᴇᴋʟᴇʀ
/bul - ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ꜱᴀʀᴋɪʟᴀʀɪ ʜɪᴢʟɪ ʙɪʀ ꜱᴇᴋɪʟᴅᴇ ɪɴᴅɪʀɪɴ
/ytplay - ʏᴏᴜᴛᴜʙᴇ'ᴅᴀɴ ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ᴍᴜᴢɪɢɪ ᴄᴀʟᴀʀ
/id - ꜱᴏʜʙᴇᴛ ɪᴅ ᴠᴇ ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ɪᴅ'ꜱɪ ʜᴀᴋᴋɪɴᴅᴀ ʙɪʟɢɪ ᴠᴇʀɪʀ
\n*🙋‍♂️ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ɪᴄɪɴ*
/durdur - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴀᴋʟᴀᴛᴍᴀ
/devam - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏᴀ ᴅᴇᴠᴀᴍ ᴇᴛ
/atla - ꜱᴏɴʀᴀᴋɪ ꜱᴀʀᴋɪʏɪ ᴄᴀʟ
/son- ᴍᴜᴢɪᴋ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴅᴜʀᴍᴀ
/asistan - ᴀꜱɪꜱᴛᴀɴɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ
/asistanby - ᴀꜱɪꜱᴛᴀɴɪɴɪᴢɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇɴ ᴄɪᴋᴀʀɪʀ
/admincache - ʏᴏɴᴇᴛɪᴍ ᴏɴ ʙᴇʟʟᴇᴋ ʏᴇɴɪʟᴇʀ
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 Müzik Kanalı", url="https://t.me/jackmedya"
                    )
                ]
            ]
        )
    )    
