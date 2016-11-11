import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COOKIES_FILE_PATH = os.path.join(BASE_DIR, "private/refresh_token.txt")

DATABASE_PATH = os.path.join(BASE_DIR, "private/database.db")

try:
    from .secret import *  # noqa
except ImportError:
    pass
