
import os
from dotenv import load_dotenv

load_dotenv()

MAPS_GEOCODING_KEY = os.getenv("maps_geocoding_key")
MAPS_JS_KEY = os.getenv("maps_js_key")
FLASK_KEY = os.getenv("flask_key")