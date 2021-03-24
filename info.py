import re
from os import environ

SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 1479154
API_HASH = '6b21cb22818e09132fb904705c31d3a1'
BOT_TOKEN = '1734210572:AAHv4jY89BZVOQ-7_MBNZekQ5XQc3QsVMoA'

# Bot settings
MAX_RESULTS = 10
CACHE_TIME = 300
USE_CAPTION_FILTER = True

# Admins, Channels & Users
ADMINS = [727037917, 'shijilraj']
CHANNELS = [-1001280193509, -1001370007665, -1001433161521, -1001457070859, -1001332267186, -1001332358174, -1001171274679, 'channelusername']
AUTH_USERS = []

# MongoDB information
DATABASE_URI = "mongodb+srv://Shijilraj:9747355576@cluster0.qwtjc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = Media Search
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I'm Media Search bot by @cinemapranthanmaar**
Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
