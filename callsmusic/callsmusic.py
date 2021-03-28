from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
def on_stream_end(chat_id: int) -> None:
    queues.task_done(chat_id)
    if queues.is_empty(chat_id):
        callsmusic.pytgcalls.join_group_call(message.chat.id)
    else:
       pytgcalls.change_stream(
        chat_id, queues.get(chat_id)["file_path"]
       )


run = pytgcalls.run
