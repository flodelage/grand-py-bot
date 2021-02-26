
from config import FLASK_KEY, MAPS_JS_KEY
from grand_py_app.views import app


app.config.update(
    DEBUG = True,
    SECRET_KEY = FLASK_KEY,
    MAPS_JS_KEY = MAPS_JS_KEY
)

if __name__ == "__main__":
    app.run()