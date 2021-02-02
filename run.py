
from grand_py_app.views import app
from env_variables import FLASK_KEY


app.config.update(
    DEBUG=True,
    SECRET_KEY=FLASK_KEY
)

if __name__ == "__main__":
    app.run()