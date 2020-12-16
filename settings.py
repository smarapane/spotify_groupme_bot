import os
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.environ.get('BOT_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')
PLAYLIST_ID = os.environ.get('PLAYLIST_ID')
GROUPME_ACCESS = os.environ.get('GROUPME_ACCESS')
