
from config import FLASK_KEY
from grand_py_app.views import app


app.config.update(
    DEBUG = False,
    SECRET_KEY = FLASK_KEY,
)

if __name__ == "__main__":
    app.run()