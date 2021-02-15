
from grand_py_app.views import app
# from env_variables import FLASK_KEY, MAPS_KEY


app.config.update(
    DEBUG=True,
    SECRET_KEY="854653653566536536363764876987080865752",
    # MAPS_KEY=MAPS_KEY
)

if __name__ == "__main__":
    app.run()