"""Initialize application."""

import os
import logging

from flask import json, Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
mm = Marshmallow()


def create_app():
    """Create Flask application."""

    # initialize app
    app = Flask(__name__)
    # and set configs
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevConfig"))
    app.url_map.strict_slashes = False  # trailing slashes unambiguity fix

    # initialize extensions
    db.init_app(app)
    mm.init_app(app)

    with app.app_context():
        # Import parts of our application
        # db.metadata.clear()
        # from .ap import dishes_view, cards_view #, routes, models

        # models are imported in api views so line above may be better below
        # together with db.create_all()

        # create db tables - models objects
        db.create_all()

        return app
