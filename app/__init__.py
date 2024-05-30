from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.models import db
from app.route import board


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(board.bp, url_prefix='/board')

    db.init_app(app)
    Migrate(app, db)

    return app
