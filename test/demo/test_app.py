# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_app.py
# Time       ：2022-05-06 17:43
# Author     ：author name
# version    ：python 3.7-32bit
# Description：测试flask app
AppContext APP
RequestContext Request
"""
from flask import Flask, current_app

app = Flask(__name__)



# 问题一： current_app做为Flask的代理对象为什么不可以使用
# 每次使用current_app的时候会执行app入栈操作，这个时候current_app才是有值的，不然这个栈顶是没有值的，所以current_app不可用
_app = current_app

with app.app_context():
    DEBUG = _app.config["DEBUG"]
    print(DEBUG)


# 问题1.1 current_app到底是什么
# current_app 包含Flask的代理的核心对象的一个上下文的代理对象，取得是localStack的栈顶。
"""
def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app
"""
