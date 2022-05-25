import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
 	CAPTION = "By [BETA BOTZ](https://t.me/beta_bot_updates)"
        PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
        PRO_USERS.append(OWNER_ID)
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "VideoWatermark_Bot")
	DATABASE_URL = os.environ.get("DATABASE_URL")
        FORCE_SUB = os.environ.get("FORCE_SUB", "beta_bot_updates")
        LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/BETA_BOTSUPPORT).__

Desgined by [BETA BOTZ](https://t.me/beta_bot_updates)
"""
	PROGRESS = """
╔═════ ⚜️ ════╗
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
╚═════ ⚜️ ════╝
"""
