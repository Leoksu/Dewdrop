from pyrogram import filters
from pyrogram import Client as ghoul
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from ..configs import USERNAME
from ..stuff.string import START_TEXT, HELP_TEXT, ABOUT_TEXT

@ghoul.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❔ HOW TO USE ME ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("📢 CHANNEL", url=f"https://t.me/TheGhostOrg"),
                InlineKeyboardButton("SOURCE 📦", url=f"https://github.com/Leoksu/Dewdrop"),
            ],
            [
                InlineKeyboardButton("🤖 ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE 🔒", callback_data="close"),
            ],
            [
                InlineKeyboardButton("➕ ADD ME TO YOUR GROUP ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
   start_markup = InlineKeyboardMarkup(buttons)
   mention = message.from_user.mention
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT.format(mention),
          reply_markup=start_markup
       )
   else:
      pm_but = [InlineKeyboardButton("PM Dew's", url="https://t.me/{USERNAME}?start")]
      pm_msg = "Hello {mention}! PM me if you have any questions on how to use me!"
      pm_markup = InlineKeyboardMarkup(pm_but)
      await message.reply_text(
          pm_msg,
          reply_markup=pm_markup
      )

@ghoul.on_callback_query()
async def cb_handler(client: ghoul, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🔙 BACK", callback_data="menu"),
                InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("🔙 BACK", callback_data="menu"),
                InlineKeyboardButton ("SUPPORT 💬", url=f"https://t.me/TheGhostSupport"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="menu":
        buttons = [
            [
                InlineKeyboardButton("❔ HOW TO USE ME ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("📢 CHANNEL", url=f"https://t.me/TheGhostOrg"),
                InlineKeyboardButton("SOURCE 📦", url=f"https://github.com/Leoksu/Dewdrop"),
            ],
            [
                InlineKeyboardButton("🤖 ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE 🔒", callback_data="close"),
            ],
            [
               InlineKeyboardButton("➕ ADD ME TO YOUR GROUP ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                MENU_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
