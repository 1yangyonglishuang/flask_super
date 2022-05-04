# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : book.py
# Time       ：2022-05-03 10:42
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from app.libs.red_print import RedPrint


api = RedPrint("book")


@api.route('/get')
def get_book():
    return "get book"


@api.route("/v1/book/create")
def create_book():
    return "create book"
