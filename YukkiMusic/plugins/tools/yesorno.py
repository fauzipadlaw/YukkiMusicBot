
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.utils.decorators.language import language
import requests
import json

### Commands
YESORNO_COMMAND = get_command("YESORNO_COMMAND")


@app.on_message(
    filters.command(YESORNO_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    yesorno=requests.get("https://yesno.wtf/api")
    data=yesorno.text
    parse_json=json.loads(data)
    image_url=parse_json['image']
    caption=parse_json['answer']
    response = await message.reply_document(
        document=image_url,
        caption=caption,
    )
