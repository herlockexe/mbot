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
\n/oynat - Mp3 Formatına uygun dosyaları çalıştırmak için deeser music destekler
/bul - istediğiniz şarkıları hızlı bir şekilde indirin
/ytplay - Youtube'dan istediğiniz müziği çalar
/id - halSohbet id ve Kullanıcının id'si kında help verir
\n*🙋‍♂️ Yalnızca yöneticiler*
/durdur - şarkı çalmayı duraklatma
/devam - şarkı çalmaya devam et
/atla - sonraki şarkıyı çal
/son- müzik çalmayı durdurma
/asistan - asistanı sohbetinize davet etme
/asistanby - Yönetici listesini yenile
/admincache - yönetim ön bellek yeniler 
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
