# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : fake.py
# Time       ：2022-05-04 15:01
# Author     ：author name
# version    ：python 3.7-32bit
# Description：离线脚本
"""
from app.app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = "super"
        user.password = "123456"
        user.email = "super@qq.com"
        user.auth = 2
        db.session.add(user)
