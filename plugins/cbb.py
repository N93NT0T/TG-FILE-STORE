# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import*


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.reply_photo(
            photo=CAPTION_ABOUT_PHOTO,
            caption=CAPTION_ABOUT, 
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
            parse_mode='html'
        )
            
        

            
    elif data == "close":
        await query.message.delete()
        await query.message.reply_photo(
            photo=CAPTION_CLOSE_PHOTO,
            caption=CAPTION_CLOSE, 
            parse_mode='html',
        )
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
