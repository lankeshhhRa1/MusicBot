from asyncio.queues import QueueEmpty
from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

import callsmusic

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("rok") & other_filters)
@errors
@authorized_users_only
async def rok(_, message: Message):
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🤐 ROK DIYA!")
        

@Client.on_message(command("fir chala") & other_filters)
@errors
@authorized_users_only
async def fir(_, message: Message):
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :-** 🥳 Fir CHala DIA vro!")


@Client.on_message(command("stop") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
        await message.reply_text(f"**{BN} :-** Thik Hai Fir , sala meri jaroorat hi nhi kisiko ")
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
            a=print("QUeuE EMpty Hai vmro")
            await message.reply_text(a)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file_path"]
            )

            await message.reply_text(f"**{BN} :-** 😬 Skip Krr Diya!")

@Client.on_message(command("Kisne Banaya Tujhe ?") & other_filters)
async def KisneBanayaTujhe(_, message: Message):
    await message.reply_text("@Lankesh_Ravan_Official SIR NE :))")

@Client.on_message(command("Shubham Bhagat Kya Hai ?") & other_filters)
async def ShubhamBhagatKyaHai(_, message: Message):
    await message.reply_text("Lodu hai Shubham toh")

@Client.on_message(command("Neem Ka Patta Kadwa Hai") & other_filters)
async def NeemKaPattaKadwaHai(_, message: Message):
    await message.reply_text("Vaibhav Dahiya Bhadwa Hai")

@Client.on_message(command("bsdk") & other_filters)
async def bsdk(_, message: Message):
    await message.reply_text("Tu bsdka , Tera Baap bsdka , Tera Dada bsdka")

@Client.on_message(command("mc") & other_filters)
async def mc(_, message: Message):
    await message.reply_text("Tu maderchod , Tera Baap maderchod , Tera Dada bhi mc")

@Client.on_message(command("bc") & other_filters)
async def bc(_, message: Message):
    await message.reply_text("Tu bhenchod , Tera Baap bhenchod , Tera Dada bhi bhenchod")

@Client.on_message(command("gandu") & other_filters)
async def gandu(_, message: Message):
    await message.reply_text("JO bolta hai wahi hota hai , aap hi gandu ho")

@Client.on_message(command("lodu") & other_filters)
async def lodu(_, message: Message):
    await message.reply_text("Tu LOdu hai mc , sudhar ja gaali mat de")

@Client.on_message(command("kaisa hai bhai") & other_filters)
async def kaisa_hai_bhai(_, message: Message):
    await message.reply_text("Lawde Lage Hai jindagi k")

@Client.on_message(command("Madhav") & other_filters)
async def madhav(_, message: Message):
    await message.reply_text("naam mat le us bsdiwale ka")
    await message.reply_text("naam mat le us bsdiwale ka dobara liya toh gand tod dunga bsdk")
    await message.reply_text("Samjha??")

@Client.on_message(command("Ha") & other_filters)
async def ha(_, message: Message):
    await message.reply_text("THIK HAI")


@Client.on_message(command("spam") & other_filters)
async def spamop(_, message: Message):
    await message.reply_text("Ravan spam OP bolte")
    await message.reply_text("Ravan spam OP bolte")
    await message.reply_text("Ravan spam OP bolte")
    await message.reply_text("Ravan spam OP bolte")
    await message.reply_text("Ravan spam OP bolte")
    await message.reply_text("Ravan spam OP bolte")

@Client.on_message(command("Ravan") & other_filters)
async def spamopp(_, message: Message):
    await message.reply_text("spam BY Ravan OP bolte")
    await message.reply_text("spam BY Ravan OP bolte")
    await message.reply_text("spam BY Ravan OP bolte")
    await message.reply_text("spam BY Ravan OP bolte")
    await message.reply_text("spam BY Ravan OP bolte")
    await message.reply_text("spam BY Ravan OP bolte")

@Client.on_message(command("Gali spam") & other_filters)
async def spamoop(_, message: Message):
    await message.reply_text("Shubham mc")
    await message.reply_text("vaibhav lodu")
    await message.reply_text("bhadwwwaa madhav")

@Client.on_message(command("Shubham mc") & other_filters)
async def spammopp(_, message: Message):
    await message.reply_text("Gali spam")
    await message.reply_text("Shubham mc")
    await message.reply_text("vaibhav lodu")
    await message.reply_text("bhadwwwaa madhav")
    
