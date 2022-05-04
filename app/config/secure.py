# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : secure.py
# Time       ：2022-05-03 10:52
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@119.91.151.142:3310/ginger'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True


SECRET_KEY = "051900abcsdafgdargdsf".encode("utf-8")