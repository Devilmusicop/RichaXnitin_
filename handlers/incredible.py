from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""Cᴏᴍᴍᴀɴᴅs ᴏғ Bᴇsᴛɪᴇs Vᴄ Bᴏᴛ 🔥🛠
**For all in group**

- `  /play <song name> - play song you requested 

- `  /song <song name> - download songs you want quickly 
