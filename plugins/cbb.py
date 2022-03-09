# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER, START_MESSAGE


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await Bot.send_photo(chat_id="me",
        photo="https://telegra.ph/file/7c5c0dc8ee6723aac16be.jpg",
        caption=START_MESSAGE,
        reply_markup=reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        parse_mode="HTML",
        disable_notification=True,
        protect_content=True
    )

            
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
