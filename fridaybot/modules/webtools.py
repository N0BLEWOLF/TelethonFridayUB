#    Copyright (C) Midhun Km 2020-2021
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

import random
import socket
import requests
from iplookup import iplookup
from selenium import webdriver
from youtube_search import YoutubeSearch
from fridaybot.function import apk_dl, Track_Mobile_Number
from fridaybot import CMD_HELP
from fridaybot.utils import edit_or_reply, friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="wshot ?(.*)"))
@friday.on(sudo_cmd(pattern="wshot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    urlissed = event.pattern_match.group(1)
    sedlyfstarky = await edit_or_reply(event, "Capturing Webshot, Stay Tuned.")
    driver = webdriver.Chrome()
    driver.get(urlissed)
    driver.get_screenshot_as_file("Webshot-@fridayot.png")
    imgpath = "Webshot-@fridayot.png"
    await sedlyfstarky.edit("Completed. Uploading in Telegram..")
    await borg.send_file(
        event.chat_id,
        file=imgpath,
        caption=f"**WEBSHOT OF** `{urlissed}` \n**Powered By @Fridayot**",
    )
    
    
@friday.on(friday_on_cmd(pattern="rmeme$"))
@friday.on(sudo_cmd(pattern="rmeme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    hmm_s = 'https://some-random-api.ml/meme'
    r = requests.get(url=hmm_s).json()
    image_s = r['image']
    await borg.send_file(event.chat_id, file=image_s, caption=r['caption'])
    

@friday.on(friday_on_cmd(pattern="lp ?(.*)"))
@friday.on(sudo_cmd(pattern="lp ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfbro = await edit_or_reply(event, "Wait Fetching Website Info")
        gone = event.pattern_match.group(1)
        url = f"https://api.ip2whois.com/v1?key=free&domain=" + gone
        await event.edit(
            "Fecthing Website Info ! Stay Tuned. This may take some time ;)"
        )
        lol = iplookup.iplookup
        okthen = lol(gone)
        sed = requests.get(url=url).json()
        km = sed["registrant"]
        kek = sed["registrar"]
        sedlyf = (
            f'Domain Name => {sed["domain"]} \nCreated On => {sed["create_date"]} \nDomain ID => {sed["domain_id"]} \nHosted ON => {kek["url"]}'
            f'\nLast updated => {sed["update_date"]} \nExpiry Date => {sed["expire_date"]} \nDomain Age => {sed["domain_age"]}'
            f'\nOwner => {km["name"]} \nCountry => {km["country"]} \nState => {km["region"]}'
            f'\nPhone Number => {km["phone"]} \nDomain Ip => {okthen}'
        )
        await tfbro.edit(sedlyf)
    except Exception:
        await tfbro.edit(f"Something Went Wrong. MayBe Website Wrong.")


@friday.on(friday_on_cmd(pattern="bin ?(.*)"))
@friday.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        tfsir = await edit_or_reply(event, "Wait Fetching Bin Info")
        kek = event.pattern_match.group(1)
        url = f"https://lookup.binlist.net/{kek}"
        midhunkm = requests.get(url=url).json()
        kekvro = midhunkm["country"]
        data_is = (
            f"<b><u>Bin</u></b> ➠ <code>{kek}</code> \n"
            f"<b><u>Type</u></b> ➠ <code>{midhunkm['type']}</code> \n"
            f"<b><u>Scheme</u></b> ➠ <code>{midhunkm['scheme']}</code> \n"
            f"<b><u>Brand</u></b> ➠ <code>{midhunkm['brand']}</code> \n"
            f"<b><u>Country</u></b> ➠ <code>{kekvro['name']} {kekvro['emoji']}</code> \n"
        )
        await tfsir.edit(data_is, parse_mode="HTML")
    except:
        await tfsir.edit("Not a Valid Bin Or Don't Have Enough Info.")


@friday.on(friday_on_cmd(pattern="iban ?(.*)"))
@friday.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    inputs = event.pattern_match.group(1)
    api = f"https://openiban.com/validate/{inputs}?getBIC=true&validateBankCode=true"
    lol = requests.get(url=api).json()
    try:
        tfhm = await edit_or_reply(event, "Wait Fetching IBAN Info")
        banks = lol["bankData"]
        kek = (
            f"<b><u>VALID</u></b> ➠ <code>{lol['valid']}</code> \n"
            f"<b><u>IBAN</u></b> ➠ <code>{lol['iban']}</code> \n"
            f"<b><u>BANK-CODE</u></b> ➠ <code>{banks['bankCode']}</code> \n"
            f"<b><u>BANK-NAME</u></b> ➠ <code>{banks['name']}</code> \n"
            f"<b><u>ZIP</u></b> ➠ <code>{banks['zip']}</code> \n"
            f"<b><u>CITY</u></b> ➠ <code>{banks['city']}</code> \n"
            f"<b><u>BIC</u></b> ➠ <code>{banks['bic']}</code> \n"
        )
        await tfhm.edit(kek, parse_mode="HTML")
    except:
        await tfhm.edit(f"Invalid IBAN Or Doesn't Have Enough Info")


@friday.on(friday_on_cmd(pattern="gitdl ?(.*)"))
@friday.on(sudo_cmd(pattern="gitdl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        kekman = await edit_or_reply(event, "Fetching Repo")
        inputs = event.pattern_match.group(1)
        sed = event.pattern_match.group(1)
        if sed:
            if " " in sed:
                stark = inputs.split(" ", 2)
        gitusername = stark[0]
        gitrepo = stark[1]
        gitbranch = stark[2]
        link = f"https://github.com/{gitusername}/{gitrepo}/archive/{gitbranch}.zip"
        await kekman.edit("Uploading... Stark Tuned.")
        await event.delete()
        await borg.send_file(event.chat_id, file=link, caption="You Repo Achieve File.")
    except:
        await borg.send_message(
            event.chat_id, "**Usage** : `.gitdl <gitusername> <gitrepo> <gitbranch>`"
        )


@friday.on(friday_on_cmd(pattern="yts ?(.*)"))
@friday.on(sudo_cmd(pattern="yts ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    try:
        fin = event.pattern_match.group(1)
        stark_result = await edit_or_reply(event, "Fectching Result this May Take Time")
        results = YoutubeSearch(f"{fin}", max_results=5).to_dict()
        noob = "<b>YOUTUBE SEARCH</b> \n\n"
        for moon in results:
            hmm = moon["id"]
            kek = f"https://www.youtube.com/watch?v={hmm}"
            stark_name = moon["title"]
            stark_chnnl = moon["channel"]
            total_stark = moon["duration"]
            stark_views = moon["views"]
            noob += (
                f"<b><u>VIDEO-TITLE</u></b> ➠ <code>{stark_name}</code> \n"
                f"<b><u>LINK</u></b> ➠ <code>{kek}</code> \n"
                f"<b><u>CHANNEL</u></b> ➠ <code>{stark_chnnl}</code> \n"
                f"<b><u>DURATION</u></b> ➠ <code>{total_stark}</code> \n"
                f"<b><u>TOTAL-VIEWS</u></b> ➠ <code>{stark_views}</code> \n\n"
            )
        await stark_result.edit(noob, parse_mode="HTML")
    except:
        await event.edit("Some Thing Went Wrong.")
        
@friday.on(friday_on_cmd(pattern="apk ?(.*)"))
async def _(event):
    akkad = event.pattern_match.group(1)
    if event.fwd_from:
        return
    pathz, name = await apk_dl(akkad, Config.TMP_DOWNLOAD_DIRECTORY, event)
    await borg.send_file(event.chat_id, pathz, caption='Uploaded By @FRidayOT')
    
@friday.on(friday_on_cmd(pattern="(numberlookup|nl) ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    hmm = "<b>Phone Info Powered By @FridayOT</b> \n\n"
    phonenumber = event.pattern_match.group(2)
    try:
        warner = Track_Mobile_Number(phonenumber).track
    except:
        await event.edit("`Failed, Please Check Phone Number.`")
        return
    for i in warner:
        hmm += f"<u><b>{i}</u></b> ➠ <code>{warner[i]}</code> \n"
    await event.edit(hmm, parse_mode="HTML")
    
@friday.on(friday_on_cmd(pattern="(comedyme|jokes)$"))
async def hehe(event):
    if event.fwd_from:
        return
    r = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()
    await event.edit(r['joke'])
    
@friday.on(friday_on_cmd(pattern="randomgif ?(.*)"))
async def gif_world(event):
    if event.fwd_from:
        return
    hu = event.pattern_match.group(2).replace(' ', '+')
    url = f"https://api.tenor.com/v1/random?q={hu}&contentfilter=medium"
    r = requests.get(url=url).json()
    await event.delete()
    giff = r["results"][random.randint(0, len(r["results"]) - 1)]["media"][0]["gif"]["url"]
    await borg.send_file(event.chat_id, giff, caption="Powered By @FridayOT")
    
@friday.on(friday_on_cmd(pattern="(randomeme|memegen)$"))
async def meme_world(event):
    if event.fwd_from:
        return
    url = f"https://some-random-api.ml/meme"
    r = requests.get(url=url).json()
    await event.delete()
    await borg.send_file(event.chat_id, r['image'], caption="**Meme Gen** - Powered By @FridayOT")
    
@friday.on(friday_on_cmd(pattern="genderguess (.*)"))
async def what(event):
    if event.fwd_from:
        return
    starky = event.pattern_match.group(1)
    url = f"https://api.diversitydata.io/?fullname={starky}"
    r = requests.get(url=url).json()
    hmm = (f"**Name :** `{r['fullname']}` \n"
           f"**Gender :** `{r['gender']}` \n"
           f"**Ethnicity :** `{r['ethnicity']}` \n"
           f"**Probability :** `{r['gender probability']}`")
    await event.edit(hmm)
     
     
@friday.on(friday_on_cmd(pattern="hostlookup (.*)"))
async def hecks(event):
    if event.fwd_from:
        return
    starky = event.pattern_match.group(1)
    try:
        kk = socket.gethostbyaddr(starky)[0]
    except:
        await event.edit("Check Your Fking IP")
        return
    await event.edit(f"**Host Name :** `{kk}`")
    
CMD_HELP.update(
    {
        "webtools": "**Web Tools**\
\n\n**Syntax : **`.wshot <website URL>`\
\n**Usage :** takes screenshot of webpage.\
\n\n**Syntax : **`.lp <URL link>`\
\n**Usage :** Gives whois information about website.\
\n\n**Syntax : **`.bin <bin>`\
\n**Usage :** Provides information about bin.\
\n\n**Syntax : **`.iban <iban>`\
\n**Usage :** Provides information about IBAN.\
\n\n**Syntax : **`.gitdl <repository name>`\
\n**Usage :** Gets repository link.\
\n\n**Syntax : **`.yts <query>`\
\n**Usage :** searches the query on YouTube and give results."
    }
)
