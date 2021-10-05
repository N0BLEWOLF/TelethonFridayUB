# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits
import io
import os

import lyricsgenius
from tswift import Song

from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

GENIUS = os.environ.get("GENIUS_API_TOKEN", None)


@friday.on(friday_on_cmd(outgoing=True, pattern="lyrics (.*)"))
@friday.on(sudo_cmd(pattern="lyrics (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "Searching For Lyrics.....")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
        await edit_or_reply(event, "`What I am Supposed to find `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try `.glyrics`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try `.glyrics`"

    if len(reply) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await edit_or_reply(event, reply)


@friday.on(friday_on_cmd(outgoing=True, pattern="glyrics(?: |$)(.*)"))
async def lyrics(lyric):
    if lyric.fwd_from:
        return
    if r"-" in lyric.text:
        pass
    else:
        await lyric.edit(
            "`Error: please use '-' as divider for <artist> and <song>`\n"
            "eg: `.glyrics Nicki Minaj - Super Bass`"
        )
        return

    if GENIUS is None:
        await lyric.edit(
            "`Provide genius access token to config.py or Heroku Config first kthxbye!`"
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = lyric.text.split(".lyrics")[1].split("-")
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception:
            await lyric.edit("`Lel please provide artist and song names`")
            return

    if len(args) < 1:
        await lyric.edit("`Please provide artist and song names`")
        return

    await lyric.edit(f"`Searching lyrics for {artist} - {song}...`")

    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None

    if songs is None:
        await lyric.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
    else:
        await lyric.edit(
            f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
        )
    return


CMD_HELP.update(
    {
        "lyric": "**Lyric**\
\n\n**Syntax : **`.lyrics <song name>`\
\n**Usage :** this plugin searches for song lyrics with song name. \
\n\n**Syntax : **`.glyrics <artist - song>`\
\n**Usage :** this plugin searches for song lyrics with song name and artist."
    }
)
