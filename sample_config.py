import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = "c2348abe-1048-4da0-915c-75e9f30b60ec"
    # get a token from @BotFather
    TG_BOT_TOKEN = "6396672577:AAFZlY6Gi17e_AlqnaRYmk3YS5gYsFLYa68"
    # your domain to show when download file is greater than MAX_FILE_SIZE
    HTTP_DOMAIN = os.environ.get("HTTP_DOMAIN", "https://example.com/")
    # for running on Heroku.com
    PORT = int(os.environ.get('PORT', 5000))
    # The Telegram API things
    APP_ID = "26489380"
    API_HASH = "4167d8b8779aab33b73810feb3c77021"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "932420516"
    # reg: Procedures
    UTUBE_BOT_USERS = AUTH_USERS
    SUPER_DLBOT_USERS = AUTH_USERS
    SUPER3X_DLBOT_USERS = AUTH_USERS
    SUPER7X_DLBOT_USERS = AUTH_USERS
    BANNED_USERS = 7351948
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
