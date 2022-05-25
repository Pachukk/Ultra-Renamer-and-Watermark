from pyrogram.errors import UserNotParticipant

async def not_subscribed(_, client, message):
   if not client.force_channel:
      return False
   try:             
      user = await client.get_chat_member(client.force_channel, message.from_user.id)
   except UserNotParticipant:
      pass
   else:
      if user.status != "kicked":
         return False 
   return True
