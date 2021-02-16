
import os
from dotenv import load_dotenv

load_dotenv()

MAPS_KEY = os.getenv("gmaps_key")
FLASK_KEY = os.getenv("flask_key")