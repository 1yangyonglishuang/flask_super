# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : __init__.py.py
# Time       ：2022-05-03 10:42
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import dataclasses
import decimal
import typing as t
import uuid
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from werkzeug.http import http_date

from app.libs.api_exceptions.api_exception import APIException


class JSONEncoder(_JSONEncoder):
    def default(self, o: t.Any) -> t.Any:

        if isinstance(o, date):
            return http_date(o)
        if isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if hasattr(o, "__html__"):
            return str(o.__html__())
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        raise APIException("serialize error")



class Flask(_Flask):
    json_encoder = JSONEncoder
