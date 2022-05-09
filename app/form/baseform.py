# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : baseform.py
# Time       ：2022-05-03 18:57
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""

from wtforms import Form

from app.libs.api_exceptions.exceptions import ParameterException


class BaseForm(Form):
    __abstract__ = True

    def __int__(self, data):
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        try:
            super(BaseForm, self).validate()
        except Exception as e:
            raise ParameterException(msg=str(e))

        is_valid = super(BaseForm, self).validate()
        if not is_valid:
            raise ParameterException(msg=self.errors)
