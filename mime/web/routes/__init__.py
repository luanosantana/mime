from flask import Flask
from mime.web.routes import root


def create_app():
    app = Flask(__name__)

    app.register_blueprint(root.bp)
    return app
