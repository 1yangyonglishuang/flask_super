# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : scope.py
# Time       ：2022-05-04 19:22
# Author     ：author name
# version    ：python 3.7-32bit
# Description：权限控制类
"""
from app.libs.api_exceptions.exceptions import Forbidden


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other: "Scope"):
        # 允许访问的api
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        # 允许访问的module
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        # 排除的api
        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class UserScope(Scope):
    allow_api = ['v1.user+get_user']


class AdminScope(Scope):
    forbidden = ['v1.user+super_user_delete']

    def __init__(self):
        pass


class SuperScope(Scope):
    allow_module = ['v1.user']


def is_in_scope(scope: str, endpoint: str):
    """
    :args: scope自定义的范围
    :args: endpoint：flask传过来的url
           blue_name.red_name+func_name
           v1.user+get_user
    """
    scope: "Scope" = globals()[scope]()
    red_name = endpoint.split("+")[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    return False


def get_scope_by_num(num: int) -> str:
    SCOPES = {
        1: "UserScope",
        2: "SuperScope",
        3: "AdminScope"
    }
    scope_str = SCOPES.get(num, None)
    if not scope_str:
        raise Forbidden

    return scope_str
