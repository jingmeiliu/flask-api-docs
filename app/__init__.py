import os

from flask import Flask

from app.extensions import bootstrap
from app.settings import config
from app.views import public_bp, docs_bp
from app.views.user import user_bp

_cache = {}


def create_app():
    app = Flask(__name__)
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])

    _cache['app'] = app

    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(public_bp, url_prefix='/public')

    app.register_blueprint(user_bp, url_prefix='/user')


def get_app():
    app = _cache['app']  # type:Flask
    return app
