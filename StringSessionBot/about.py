<<<<<<< HEAD
from pyLegendSS.Data import Data
=======
from Stringss.Data import Data

# Import other necessary modules
>>>>>>> 4c2a2ebd7331c35e9afbce1d9cf0d82854682ef9
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )

