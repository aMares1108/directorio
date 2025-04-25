from flask import Flask
from flask_login import LoginManager
from .config import Config
from .extensions import db
from .blueprints import register_blueprints
from dotenv import load_dotenv
from logging import getLogger
from os import getenv, urandom

LOGGER = getLogger(__name__)

LOGGER.debug(load_dotenv())
LOGGER.debug(getenv('MYSQL_URI'))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.secret_key = urandom(32)

    # Inicializar extensiones
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'register.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar blueprints
    register_blueprints(app)

    return app
