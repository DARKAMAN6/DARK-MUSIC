# Originally written by levina on github
# Broadcast function


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from KennedyMusic.callsmusic.callsmusic import client as Bot
from KennedyMusic.config import SUDO_USERS

@Client.on_message(filters.command(["dcast"]))
async def dcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`πππ°πππΈπ½πΆ ππ²π°πππ₯`")
        if not message.reply_to_message:
            await wtf.edit("πΏπ»π΄π°ππ΄ ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄ ππΎ πππ°ππ ππ²π°ππ!")
            return
        lmao = message.reply_to_message.text
        async for dialog in Bot.iter_dialogs():
            try:
                await Bot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`ππ΄π½πΎπΌπππ₯` \n\n**ππ΄π½π ππΎ β** `{sent}` π²π·π°ππ \n**π΅π°πΈπ»π΄π³ πΈπ½ β** {failed} π²π·π°ππ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`ππ²π°ππ πππ²π²π΄ππ΅ππ»π»π π₯` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
