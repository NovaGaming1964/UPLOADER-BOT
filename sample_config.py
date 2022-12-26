import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "2060294496:AAHpy_RP3U99VQHOhwjDj4JJR0F0ddrpSYA"
    # The Telegram API things
    APP_ID = 7022264
    API_HASH = "6595dfeaed73a28f66c4a923f7f452ef"
    # Get these values from my.telegram.org
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = 128
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # your telegram id
    OWNER_ID = 1695220698
    # database session name, example: xurluploader
    SESSION_NAME = "URL-UPLOADER"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://ghostsniper:ghostsniper7@cluster0.72mwp.mongodb.net/?retryWrites=true&w=majority"
