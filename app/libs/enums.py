# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : enums.py
# Time       ：2022-05-03 12:16
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_PHONE = 101

    USER_MINA = 200
    USER_WX = 201


class ScopeTypeEnum(Enum):
    ADMIN_SCORE = 3
    SUPER_SCORE = 2
    USER_SCORE = 1


