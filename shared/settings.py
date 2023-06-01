import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# LINE
LINE_CHANNEL_SECRET = os.environ.get(
    "LINE_CHANNEL_SECRET", os.getenv("LINE_CHANNEL_SECRET"))
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get(
    "LINE_CHANNEL_ACCESS_TOKEN", os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
ENV = os.environ.get("ENV")
