from os import getenv
from dotenv import load_dotenv

load_dotenv()

HOSTNAME = getenv("HOSTNAME")
PORT = getenv("PORT")
DATABASE_URI = getenv("DATABASE_URI")
MODELS_PATH = getenv("MODELS_PATH")

RELOAD = getenv("RELOAD")
LOGLEVEL = getenv("LOGLEVEL")
