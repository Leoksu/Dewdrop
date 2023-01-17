from pyrogram import Client as ghoul
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from ..configs import USERNAME

@ghoul.on_message(filters.command(["help", "help@{USERNAME}"]))
async def help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔙 BACK", callback_data="start"),
            InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
        ]
        ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if message.chat.type == 'private':
        await message.reply_text(
            HELP_TEXT,
            reply_markup=reply_markup
        )
    else:
        pm_but = [InlineKeyboardButton("PM Dew's", url="https://t.me/{USERNAME}?start")]
        pm_msg = "Hello! PM me if you have any questions on how to use me!"
        pm_markup = InlineKeyboardMarkup(pm_but)
        await message.reply_text(
            pm_msg,
            reply_markup=pm_markup
        )
