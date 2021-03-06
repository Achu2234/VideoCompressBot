#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @hackelite01

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, \n\nThis is a Telegram <b>Video Compressor Bot</b>. \n\n<b>Please send me any Telegram big video file I will compress it as s small video file!</b> \n\n/help for more details. \n\n<b>You must subscribe our channel in order to use me😇</b>"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "ðŸ“¥ Downloading ... ðŸ“¥ \n"
    
    UPLOAD_START = "ðŸ“¤ Uploading ... ðŸ“¤ \n"
    
    COMPRESS_START = "ðŸ“€ Trying to compress ... ðŸ“€"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "ðŸ“¥ Downloaded in {}\n\nðŸ“€ Compressed in {}\n\nðŸ“¤ Uploaded in {}\n\nBy @VKPROJECTS"

    COMPRESS_PROGRESS = "â„1¤7 ETA: {}\nðŸš€ Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "âœ„1¤7 Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "âœ„1¤7 Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "âœ„1¤7 Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "âš ï¸ Already one Process going on! âš ï¸ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport : @VKPROJECTS"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
