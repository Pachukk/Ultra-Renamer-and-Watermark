from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    await add_user_to_database(c, m)
    await m.reply_photo(
       photo="https://telegra.ph//file/69b6154eaecdaf3845d9f.jpg",
       caption=f"""👋 Hai {m.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! \n𝙱𝙾𝚃 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢: <a href=https://t.me/beta_bot_updates>βΣTΔ βΩTZ</a> \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("♀️ OWNER ♀️", url='https://t.me/JP_Jeol_org')
          ],[
          InlineKeyboardButton('🤖 UPDATES', url='https://t.me/beta_bot_updates'),
          InlineKeyboardButton('💥 SUPPORT', url='https://t.me/BETA_BOTSUPPORT')
          ],[
          InlineKeyboardButton('⚙️ SETTING', callback_data='showSettings')
          ]]
          )
       )
    


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="I can rename media without downloading it!\n"
             "Speed depends on your media DC.\n\n"
             "Just send me media and reply to it with /rename command.\n\n"
             "To set custom thumbnail reply to any image with /set_thumbnail\n\n"
             "To see custom thumbnail press /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Show Settings",
                                      callback_data="showSettings")]])
    )
