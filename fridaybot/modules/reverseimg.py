# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Thanks to @kandnub, for this awesome module !!
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for reverse searching stickers and images on Google """

import io
import os
import re
import urllib
import shutil
from re import findall
import requests
from bs4 import BeautifulSoup
from PIL import Image
from fridaybot.function.gmdl import googleimagesdownload
from fridaybot import CMD_HELP
from fridaybot.utils import errors_handler, register, friday_on_cmd

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@friday.on(friday_on_cmd(pattern=r"reverse(?: |$)(\d*)"))
async def okgoogle(img):
    if img.fwd_from:
        return
    """ For .reverse command, Google search images and stickers. """
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    event = img
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Reply to photo or sticker nigger.`")
        return

    if photo:
        await img.edit("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await img.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            await img.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Looking for this Image...`")
        else:
            await img.edit("`Can't find this piece of shit.`")
            return
        lim = findall(r"lim=\d+", guess)
        try:
            lim = lim[0]
            lim = lim.replace("lim=", "")
            guess = guess.replace("lim=" + lim[0], "")
        except IndexError:
            lim = 5
        response = googleimagesdownload()
        logger.info(guess)
        arguments = {
            "keywords": guess,
            "silent_mode": True,
            "limit": lim,
            "format": "jpg",
            "no_directory": "no_directory",
        }
        paths = response.download(arguments)
        lst = paths[0][guess]
        await event.edit(f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})")
        await event.client.send_file(
            await event.client.get_input_entity(event.chat_id), lst
        )
        shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


CMD_HELP.update(
    {
        "reverse": ".reverse\
        \nUsage: Reply to a pic/sticker to revers-search it on Google Images !!"
    }
)
