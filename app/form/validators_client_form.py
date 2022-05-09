# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : validators_client_form.py
# Time       ：2022-05-03 12:18
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.form.baseform import BaseForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(), length(min=6, max=20)])

    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value: ClientTypeEnum):
        try:
            client = ClientTypeEnum(value.data)
            self.type.data = client
        except ValidationError as e:
            raise ValidationError(e)


class UserEmailForm(ClientForm):
    account = EmailField(validators=[Email(message="invalidate email")])
    secret = StringField(validators=[DataRequired(), Regexp(
        r"^[A-Za-z0-9_*&#@]{6,22}$", message="密码长度需要大于6为且小于22位")])
    nickname = StringField(validators=[length(min=0, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first() is not None:
            raise ValidationError("当前邮箱已经被注册了")
