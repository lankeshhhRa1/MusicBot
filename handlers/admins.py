from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🤐 ROK DIYA!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🥳 RESUME KRR DIA!")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :-** ❌ KHATAM TATA GOOD BYE GAYA!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            await message.reply_text("Are bhai queue empty hai,kuch de toh sahi bjane ko")
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

        await message.reply_text(f"**{BN} :-** 😬 Skip Krr Diya!")

@Client.on_message(command("Ravan") & other_filters)
async def Ravan(_, message: Message):
    await message.reply_text("KYA HUA SIR,AAB KYA KIYA MAINE ?")

@Client.on_message(command("KisneBanayaTujhe") & other_filters)
async def KisneBanayaTujhe(_, message: Message):
    await message.reply_text("@Lankesh_Ravan_Official SIR NE :))")

@Client.on_message(command("ShubhamBhagatKyaHai") & other_filters)
async def ShubhamBhagatKyaHai(_, message: Message):
    await message.reply_text("Lodu hai Shubham toh")

@Client.on_message(command("NeemKaPattaKadwaHai") & other_filters)
async def NeemKaPattaKadwaHai(_, message: Message):
    await message.reply_text("Vaibhav Dahiya Bhadwa Hai")



