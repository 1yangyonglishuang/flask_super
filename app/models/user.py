# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : user.py
# Time       ：2022-05-03 12:43
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.api_exceptions.exceptions import NotFundException, AuthException
from app.models.base import Base, db
from app.models.article import Article


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(128))
    face = Column(String(128), default="")

    def keys(self):
        return ["id", "email", "nickname", "auth"]

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        if nickname is None:
            nickname = account
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise NotFundException()
        if not user.check_password(password):
            raise AuthException()

        return {"uid": user.id, "scope": user.auth}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)


