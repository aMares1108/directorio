from flask import Flask
from .config import Config
from .extensions import db
from .blueprints import register_blueprints
from dotenv import load_dotenv
from logging import getLogger
from os import getenv

LOGGER = getLogger(__name__)

LOGGER.debug(load_dotenv())
LOGGER.debug(getenv('MYSQL_URI'))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Registrar blueprints
    register_blueprints(app)

    return app
