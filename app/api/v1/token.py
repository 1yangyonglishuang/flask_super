# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : token.py
# Time       ：2022-05-03 22:41
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from flask import request

from app.form.validators_client_form import ClientForm
from app.libs.enums import ClientTypeEnum
from app.libs.jwt_token import generate_payload, generate_token
from app.libs.red_print import RedPrint
from app.libs.success import Success
from app.models.user import User

api = RedPrint("token")


@api.route("/", methods=["POST"])
def get_token():
    data = request.json
    client_form = ClientForm(data=data)
    client_form.validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }

    identity: dict = promise[client_form.type.data](
        client_form.account.data, client_form.secret.data)

    token = _generate_auth_token(identity.get("uid"),
                                 client_form.type.data.value,
                                 identity['scope'],
                                 expiration=7200)
    return Success(msg=token)


def _generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    payload = generate_payload(uid=uid, ac_type=ac_type, scope=scope)
    return generate_token(payload, expiry=expiration)
