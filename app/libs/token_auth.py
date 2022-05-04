# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : token_auth.py
# Time       ：2022-05-04 0:09
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from collections import namedtuple

from flask import g, request
from flask_httpauth import HTTPBasicAuth

from app.libs.jwt_token import verify_token
from app.libs.scope import is_in_scope, get_scope_by_num
from app.models.user import User

auth = HTTPBasicAuth()
_User = namedtuple("User", ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password=None):
    payload = verify_token(token)
    uid = payload.get('uid')
    user = User.query.filter_by(id=uid).first_or_404_for_api()
    scope = get_scope_by_num(user.auth)

    userinfo = _User(payload.get('uid'), payload.get('ac_type'), scope)
    is_scope = True if is_in_scope(scope, request.endpoint) else False

    if not userinfo:
        return False
    g.user = userinfo
    return True and is_scope
