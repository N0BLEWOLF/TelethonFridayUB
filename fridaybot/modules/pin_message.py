"""Pins the replied message
Syntax: .cpin [LOUD]"""
from telethon.tl import functions

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("cpin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    silent = True
    input_str = event.pattern_match.group(1)
    if input_str:
        silent = False
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await borg(
                functions.messages.UpdatePinnedMessageRequest(
                    event.chat_id, message_id, silent
                )
            )
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.delete()
    else:
        await event.edit("Reply to a message to pin the message in this Channel.")


CMD_HELP.update(
    {
        "pin_message": "**pin Message**\
\n\n**Syntax : **`.cpin <reply to a message>`\
\n**Usage :** Replyed message is pinned."
    }
)
