# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : __init__.py.py
# Time       ：2022-05-03 10:42
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from flask import Blueprint, Flask
from app.api.v1 import user, book, client, token

app = Flask(__name__)


def register_blueprint_v1() -> Blueprint:
    v1_blueprint = Blueprint("v1", __name__)

    user.api.register(v1_blueprint)
    book.api.register(v1_blueprint)
    client.api.register(v1_blueprint)
    token.api.register(v1_blueprint)

    return v1_blueprint
