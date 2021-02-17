
import os
from dotenv import load_dotenv

load_dotenv()

MAPS_GEOCODING_KEY = os.getenv('MAPS_GEOCODING_KEY')
MAPS_JS_KEY = os.getenv('MAPS_JS_KEY')
FLASK_KEY = os.getenv('FLASK_KEY')

# MAPS_GEOCODING_KEY = os.environ("MAPS_GEOCODING_KEY")
# MAPS_JS_KEY = os.environ("MAPS_JS_KEY")
# FLASK_KEY = os.environ("FLASK_KEY")
