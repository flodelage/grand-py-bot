
from grand_py_app.views import app
from env_variables import FLASK_KEY, MAPS_KEY


app.config.update(
    DEBUG=False,
    SECRET_KEY=FLASK_KEY,
    MAPS_KEY=MAPS_KEY
)

if __name__ == "__main__":
    app.run()