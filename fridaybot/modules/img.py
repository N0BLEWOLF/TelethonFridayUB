"""Download & Upload Images on Telegram\n
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded and Google Image Error Fixed
"""

import os
import shutil
from re import findall

from fridaybot import CMD_HELP
from fridaybot.function.gmdl import googleimagesdownload
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="(img|image|googleimage|gi) ?(.*)"))
@friday.on(sudo_cmd(pattern="(img|image|googleimage|gi) ?(.*)", allow_sudo=True))
async def img_sampler(event):
    await edit_or_reply(event, "`Processing...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        query = reply.message
    else:
        await edit_or_reply(
            event, "`um, mind mentioning what I actually need to search for ;_;`"
        )
        return

    lim = findall(r"lim=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()
    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "silent_mode": True,
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()


CMD_HELP.update(
    {
        "img": "**Img**\
\n\n**Syntax : **`.img <query>`\
\n**Usage :** get images just with a query"
    }
)
