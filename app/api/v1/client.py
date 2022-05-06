# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : client.py
# Time       ：2022-05-03 12:34
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from flask import request, jsonify
from app.form.validators_client_form import ClientForm, UserEmailForm
from app.libs.api_exceptions.exceptions import ClientException
from app.libs.enums import ClientTypeEnum
from app.libs.red_print import RedPrint
from app.libs.success import Success
from app.libs.token_auth import auth
from app.models.user import User

api = RedPrint("client")


@api.route('/register', methods=['GET', 'POST'])
def create_client():
    data = request.json
    client_form = ClientForm(data=data)

    client_form.validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email
    }
    promise[client_form.type.data]()
    return Success()


def _register_user_by_email():
    email_form = UserEmailForm(data=request.json)

    email_form.validate_for_api()
    User.register_by_email(
        account=email_form.account.data,
        secret=email_form.secret.data,
        nickname=email_form.nickname.data)


