from pyrogram import Client, filters, enums
from helper.database import AshutoshGoswami24


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__𝗚𝗶𝘃𝗲 𝗧𝗵𝗲 𝗣𝗿𝗲𝗳𝗶𝘅__\n\n𝗘𝘅𝗮𝗺𝗽𝗹𝗲:- `/set_prefix @PandaWep`**")
    prefix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    await AshutoshGoswami24.set_prefix(message.from_user.id, prefix)
    await SnowDev.edit("**ᴘʀᴇғɪx sᴀᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    prefix = await AshutoshGoswami24.get_prefix(message.from_user.id)
    if not prefix:
        return await SnowDev.edit("**You Don't Have Any Prefix ❌**")
    await AshutoshGoswami24.set_prefix(message.from_user.id, None)
    await SnowDev.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    prefix = await AshutoshGoswami24.get_prefix(message.from_user.id)
    if prefix:
        await SnowDev.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await SnowDev.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__𝗚𝗶𝘃𝗲 𝗧𝗵𝗲 𝗦𝘂𝗳𝗳𝗶𝘅__\n\nExample:- `/set_suffix @PandaWep`**")
    suffix = message.text.split(" ", 1)[1]
    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    await AshutoshGoswami24.set_suffix(message.from_user.id, suffix)
    await SnowDev.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    suffix = await AshutoshGoswami24.get_suffix(message.from_user.id)
    if not suffix:
        return await SnowDev.edit("**You Don't Have Any Suffix ❌**")
    await AshutoshGoswami24.set_suffix(message.from_user.id, None)
    await SnowDev.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    SnowDev = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    suffix = await AshutoshGoswami24.get_suffix(message.from_user.id)
    if suffix:
        await SnowDev.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await SnowDev.edit("**You Don't Have Any Suffix ❌**")










#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot