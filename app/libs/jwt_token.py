# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : jwt_token.py
# Time       ：2022-05-03 23:03
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import datetime
import typing as t
import jwt
from dataclasses import dataclass
from flask import current_app
from jwt import ExpiredSignatureError, DecodeError
from app.libs.api_exceptions.exceptions import JWTVerifyException


@dataclass
class JWTPayload:
    uid: int
    auth: str = 'blue'
    scope: str = 1
    ac_type: str = 'email'


def generate_payload(uid, auth=None, scope=None, ac_type="email"):
    return JWTPayload(uid, auth, scope, ac_type).__dict__


def generate_token(payload: dict, expiry: int, secret=None):
    _payload = {"exp": datetime.datetime.now() + datetime.timedelta(seconds=expiry)}
    _payload.update(payload)
    if not secret:
        secret = current_app.config["SECRET_KEY"]
    return jwt.encode(_payload, secret, algorithm="HS256")


def verify_token(token, secret=None):
    if not secret:
        secret = current_app.config["SECRET_KEY"]
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
    except ExpiredSignatureError:
        raise JWTVerifyException("当前jwt已经过期了")
    except DecodeError:
        raise DecodeError("jwt decode error")

    return payload
