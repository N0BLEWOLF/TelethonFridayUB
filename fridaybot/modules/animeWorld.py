#    Copyright (C) @chsaiujwal 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from anime_downloader.sites import get_anime_class

from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd

from mal import AnimeSearch, Anime, MangaSearch, Manga

@friday.on(friday_on_cmd(pattern="anime ?(.*)"))
@friday.on(sudo_cmd(pattern="anime ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ommhg = await edit_or_reply(event, "Searching For Anime.....")
    lmao = input_str.split(":", 1)
    try:
       site = lmao[1]
    except:
       site = "animeonline360"
       await edit_or_reply(event, "Please Provide Site Name From Next Time. Now Continuing With Default Site.")

    lol = lmao[0]
    why = site.lower()

    Twist = get_anime_class(why)
    try:
       search = Twist.search(lol)
    except:
       await ommhg.edit("Please Try Different Site. Given Site Is Down.")

    title1 = search[0].title
    url1 = search[0].url
    title2 = search[1].title
    url2 = search[1].url
    title3 = search[2].title
    url3 = search[2].url
    title4 = search[3].title
    url4 = search[3].url
    title5 = search[4].title
    url5 = search[4].url
    NopZ = f"<b><u>Anime Search Complete</b></u> \n\n\n<b>Title</b>:-  <code>{title1}</code> \n<b>URL Link</b>:- {url1}\n\n<b>Title</b>:-  <code>{title2}</code> \n<b>URL Link</b>:- {url2}\n\n<b>Title</b>:-  <code>{title3}</code>\n<b>URL Link</b>:- {url3}\n\n<b>Title</b>:-  <code>{title4}</code> \n<b>URL Link</b>:- {url4}\n\n<b>Title</b>:-  <code>{title5}</code> \n<b>URL Link</b>:- {url5}\n\n<b>Links Gathered By Friday\nGet Your Own Friday From @FRIDAYCHAT</b>"
    await borg.send_message(event.chat_id, NopZ, parse_mode="HTML",)
    await ommhg.delete()


@friday.on(friday_on_cmd(pattern="ainfo ?(.*)"))
@friday.on(sudo_cmd(pattern="ainfo ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    Zp = await edit_or_reply(event, "Please Wait....🚶‍♂️🚶‍♂️🚶‍♂️")
    search = AnimeSearch(input_str)
    ID = search.results[0].mal_id
    anime = Anime(ID)
    jp = ""
    for x in anime.genres:
      jp += x + ";  "
    link = anime.image_url
    if link == None:
      link = search.results[0].image_url
    By = f"""<u><b>Anime Information Gathered</b></u>
<b>tlele:- {search.results[0].title}
Mal ID:- {search.results[0].mal_id}
Url:- {search.results[0].url}
Type:- {search.results[0].type}
Episodes:- {search.results[0].episodes}
Score:- {search.results[0].score}
Synopsis:- {search.results[0].synopsis}
Status:- {anime.status}
Genres:- {jp}
Duration:- {anime.duration}
Popularity:- {anime.popularity}
Rank:- {anime.rank}
favorites:- {anime.favorites}</b>
"""
    await borg.send_message(
        event.chat_id,
        By,
        parse_mode="HTML",
        file=link,
        force_document=False,
        silent=True,
    )
    await Zp.delete()


@friday.on(friday_on_cmd(pattern="manga ?(.*)"))
@friday.on(sudo_cmd(pattern="manga ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    LeO = await edit_or_reply(event, "Please Wait....🚶‍♂️🚶‍♂️🚶‍♂️")
    search = MangaSearch(input_str)
    ID = search.results[0].mal_id
    manga = Manga(ID)
    jp = ""
    for x in manga.genres:
      jp += x + ";  "
    link = manga.image_url
    if link == None:
      link = search.results[0].image_url
    By = f"""<u><b>manga Information Gathered</b></u>
<b>tlele:- {search.results[0].title}
Mal ID:- {search.results[0].mal_id}
Url:- {search.results[0].url}
Type:- {search.results[0].type}
volumes:- {search.results[0].volumes}
Score:- {search.results[0].score}
Synopsis:- {search.results[0].synopsis}
Status:- {manga.status}
Genres:- {jp}
Chapters:- {manga.chapters}
Popularity:- {manga.popularity}
Rank:- {manga.rank}
favorites:- {manga.favorites}</b>
"""
    await borg.send_message(
        event.chat_id,
        By,
        parse_mode="HTML",
        file=link,
        force_document=False,
        silent=True,
    )
    await LeO.delete()




CMD_HELP.update(
    {
        "animeWorld": "**Anime World**\
\n\n**Syntax : **`.ainfo <Amime Name>`\
\n**Usage :** Gives anime information.\
\n\n**Syntax : **`.manga <Amime Name>`\
\n**Usage :** Gives manga information.\
\n\n**Syntax : **`.anime <Amime Name:site Name>`\
\n**Usage :** Automatically Gets Streaming Link Of The Anime.\
\n**Example :** `.anime one piece:animeonline360`\
\n**Note** :** Get Site names list from [Here](https://devsexpoanime.netlify.app/)."
    }
)
