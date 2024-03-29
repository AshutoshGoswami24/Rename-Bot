import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot

class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @PandaWep"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/PandaWep>𝗣𝗮𝗻𝗱𝗮𝗪𝗲𝗽</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/AshutoshGoswami24>𝗔𝘀𝗵𝘂𝘁𝗼𝘀𝗵 𝗚𝗼𝘀𝘄𝗮𝗺𝗶</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/AshutoshGoswami24>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/AshutoshGoswami24>Developer</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @PandaWep
╰━━━━━━━━━━━━━━━➣ </b>"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    DONATE_TXT = """
<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> `PandaWep@ybl`
"""

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
