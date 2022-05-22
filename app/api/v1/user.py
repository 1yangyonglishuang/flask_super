# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : user.py
# Time       ：2022-05-03 10:42
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

from app.libs.red_print import RedPrint
from flask import jsonify, g, request

from app.libs.success import DeleteSuccess
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = RedPrint("user")


@api.route("/<int:uid>")
@auth.login_required
def super_user_delete(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404_for_api()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=["GET"])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404_for_api()
    return jsonify(user)


@api.route('', methods=["DELETE"])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404_for_api()
        user.delete()
    return DeleteSuccess()


@api.route("/create", methods=["POST"])
def create_user():
    data = request.json
    with db.auto_commit():
        user = User()
        user.nickname = data.get('nickname')
        user.email = data.get('account')
        user.password = data.get('secret')
        db.session.add(user)

    return "create user"
