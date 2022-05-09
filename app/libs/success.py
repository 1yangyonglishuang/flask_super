# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : success.py
# Time       ：2022-05-03 21:41
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from app.libs.api_exceptions.api_exception import APIException


class Success(APIException):
    msg = 'ok'
    error_code = -2
    code = 200


class DeleteSuccess(Success):
    msg = "delete ok"
    code = 202
    error_code = -1
