import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("28381389", ""))
API_HASH = getenv("c7bb99c961b6358cd1a185010c6260e6", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7105102714:AAE0dNwTNk7wApKlOhPqoM_4d7owXqKmDJM", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://bossmongo6175:bossmongo6175@cluster0.nveyjvf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002125362647", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5884723781"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://t.me/Coders_Alliance", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Meetup_Zone")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/Meetup_Zone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGxEM0AGZZbfeWMNCcZ3n8zOv4KwnyOUEyZ8nmNkqDic3g9GeGOP0lQvtcu9SvQHOyIYQhDJyGhRIXGj6rSF_SRxdXX7Yp0ybWp1b5_r4XPK0mWHZBV6r2_wRslx6mtBgn_jSAoMnnSoEq6Pgo3mxmI514ksX6cS9lf9Eb06P0NIsk6PJ2vrJbQbvT6A-eeFiW7GbDNf_CZAKMstbmuL9ErQEsMxFO4RBIP1go5qbPiPiPKR4d3aZ22EFhAttWwY879Jt35DMW4kychb5_PpICrqeOrB_tkyRdgp4hCZ-aU_Lb8waTD4ZeaUKkkpTkqIWSTMJr4dGNv_St001feXLsYrfDwvAAAAAFKq2dDAA", None)
STRING2 = getenv("BQGxEM0AGZZbfeWMNCcZ3n8zOv4KwnyOUEyZ8nmNkqDic3g9GeGOP0lQvtcu9SvQHOyIYQhDJyGhRIXGj6rSF_SRxdXX7Yp0ybWp1b5_r4XPK0mWHZBV6r2_wRslx6mtBgn_jSAoMnnSoEq6Pgo3mxmI514ksX6cS9lf9Eb06P0NIsk6PJ2vrJbQbvT6A-eeFiW7GbDNf_CZAKMstbmuL9ErQEsMxFO4RBIP1go5qbPiPiPKR4d3aZ22EFhAttWwY879Jt35DMW4kychb5_PpICrqeOrB_tkyRdgp4hCZ-aU_Lb8waTD4ZeaUKkkpTkqIWSTMJr4dGNv_St001feXLsYrfDwvAAAAAFKq2dDAA", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STATS_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
