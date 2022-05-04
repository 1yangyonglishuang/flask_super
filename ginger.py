# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : secure.py
# Time       ：2022-05-03 10:52
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.api_exceptions.api_exception import APIException

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        return APIException(str(e))


if __name__ == '__main__':
    app.run(debug=True)
