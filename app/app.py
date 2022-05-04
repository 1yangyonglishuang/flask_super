# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : app.py
# Time       ：2022-05-03 10:53
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

from app import Flask
from app.api.v1 import register_blueprint_v1


def _register_blueprint(app: Flask):
    app.register_blueprint(register_blueprint_v1(), url_prefix="/v1")


def _register_plugin(app: Flask):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.settings')
    _register_blueprint(app)
    _register_plugin(app)
    return app
