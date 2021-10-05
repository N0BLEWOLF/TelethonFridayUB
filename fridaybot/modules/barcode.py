"""BarCode Generator
Command .barcode (your text)
By @snappy101
"""

import asyncio
import os
from datetime import datetime

import barcode
from barcode.writer import ImageWriter
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd

from fridaybot import CMD_HELP


@friday.on(friday_on_cmd(pattern="barcode ?(.*)"))
@friday.on(sudo_cmd(pattern="barcode ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "...")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.barcode <long text to include>`"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await borg.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await edit_or_reply(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await edit_or_reply(event, "Created BarCode in {} seconds".format(ms))
    await asyncio.sleep(5)
    await event.delete()


CMD_HELP.update(
    {
        "barcode": "**Barcode**\
\n\n**Syntax : **`.barcode <text>`\
\n**Usage :** Creates Barcode Of Your Text."
    }
)
