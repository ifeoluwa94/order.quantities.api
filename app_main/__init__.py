from flask import Flask
from app_main.Utils.database_scripts import CREATE_DATABASE_SCHEMA
import sqlite3

"""Create sqlite database connection and make it globally available"""
db = sqlite3.connect("Database/order.sqlite")


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.executescript(CREATE_DATABASE_SCHEMA)

    with app.app_context():
        # Import Routes
        from app_main.Routes import routes

        # Register Blueprints
        app.register_blueprint(routes.route_bp, url_prefix='/')
        return app


init_app()
