from flask import Flask

from backend.app import database
from backend.app.config import get_config
from backend.app.errors import register_error_handlers
from backend.app.logger import get_logger
from backend.app.routes import register_routes

logger = get_logger(__name__)


def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    database.init_app(app)
    register_routes(app)
    register_error_handlers(app)

    logger.info("Application created (env=%s)", config_name or "default")
    return app
