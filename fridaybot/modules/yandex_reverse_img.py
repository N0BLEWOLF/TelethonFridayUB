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

import os
import requests
from fridaybot import CMD_HELP
from fridaybot.function import convert_to_image
from fridaybot.utils import friday_on_cmd, sudo_cmd
import json
import requests
sedpath = "./yandex/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

@friday.on(friday_on_cmd(pattern=r"yandex"))
@friday.on(sudo_cmd(pattern=r"yandex", allow_sudo=True))
async def hmm(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    hmmu = await event.reply("hmm... Reverse Searching The Image On Yandex...🚶")
    sed = await event.get_reply_message()
    img = await convert_to_image(event, borg)
    filePath = img
    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    caption = f"""<b>Reverse Search Conpleted!</b>

Reverse Searched Link:- {img_search_url}

Note:- Yandex is a Russian search engine, so better open link in chrome with auto-translate.

Another Note:- Don't Use This Command continually, Yandex Will Block Your Request.


<u><b>Reverse Search Completed By Friday.
Get Your Own Friday From @FRIDAYCHAT.</b></u>

"""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )
    await event.delete()
    

CMD_HELP.update(
    {
        "yandex_reverse_img": "**Yandex Reverse Image search**\
\n\n**Syntax : **`.yandex <reply to image>`\
\n**Usage :** Reverse Searches The Image on yandex."
    }
)

