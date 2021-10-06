try:
    from PIL import Image
except ImportError:
    import Image

import os

import pytesseract

from fridaybot import CMD_HELP
from fridaybot.Configs import Config
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="read$"))
async def _(event):
    global images
    if event.fwd_from:
        return
    await event.edit("`Reading, Please Wait..`")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        imagez = await borg.download_media(
            await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
        )
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
    results = pytesseract.image_to_string(Image.open(imagez))
    mk = f"<b><u> OCR </u></b> \n<b></u>Here is What I Can Read From This.</u></b> \n<code>{results}</code>"
    await event.edit(mk, parse_mode="HTML")
    if os.path.exists(results):
        os.remove(results)


CMD_HELP.update(
    {
        "pyocr": "**PY OCR**\
\n\n**Syntax : **`.read <reply to image>`\
\n**Usage :** it automatically reads the image and shows text in the image."
    }
)
