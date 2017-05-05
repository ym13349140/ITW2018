#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # Register all the filter.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .travel import travel as travel_blueprint
    app.register_blueprint(travel_blueprint)
    # from .user import user as user_blueprint
    # app.register_blueprint(user_blueprint, url_prefix='/user')

    return app

