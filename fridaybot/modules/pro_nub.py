"""Available Commands:

.unoob
.menoob
.upro
.mepro

@arnab431"""


import asyncio

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "unoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL YoU aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@friday.on(friday_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "menoob":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "BiGGeSt",
            "NoOoB",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ BiGGeSt NoOoB uNtiL i aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)


@friday.on(friday_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "upro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "YoU",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL YoU aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)


@friday.on(friday_on_cmd("(.*)"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "iZ",
            "PeRu",
            "uNtiL",
            "i",
            "aRriVe",
            "😈",
            "EvErYbOdY iZ PeRu uNtiL i aRriVe 😈",
        ]

        for i in animation_ttl:

            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)


CMD_HELP.update(
    {
        "pro_nub": "**Pro noob**\
\n\n**Syntax : **`.unoob`\
\n**Usage :** funny prank plugin to show others as noobs.\
\n\n**Syntax : **`.menoob`\
\n**Usage :** funny prank plugin to show yourself as noob.\
\n\n**Syntax : **`.upro`\
\n**Usage :** funny prank plugin to show others as pros.\
\n\n**Syntax : **`.mepro`\
\n**Usage :** Funny plugin to show yourself as pro."
    }
)
