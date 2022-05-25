import logging 
import logging.config
from typing import Union
from pyromod import listen
from pyrogram import Client as RawClient
from pyrogram.storage import Storage
from configs import Config
from bot.core.new import New

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR) 



class Client(RawClient, New):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "RenameBot"):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="bot/plugins"
            )
        )

    async def start(self):
       await super().start()
       me = await self.get_me() 
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = Config.FORCE_SUB
       if Config.FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(Config.FORCE_SUB)
            self.invitelink = link
         except Exception as e:
            logging.warning(e) 
            logging.warning("Make Sure Bot admin in force sub channel") 
            self.force_channel = None
       logging.info(f"{me.first_name} Started")
        
    async def stop(self, *args):
      await super().stop()
      logging.info("Bot Stopped")





