# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : red_print.py
# Time       ：2022-05-03 11:20
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import typing as t
from flask import Blueprint


class RedPrint(object):

    def __init__(self, name):
        self.name = name
        self.bound = []

    def register(self, bp: Blueprint, url_prefix=None):
        if url_prefix is None:
            url_prefix = self.name
        for f, rule, options in self.bound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

    def route(self, rule: str, **options: t.Any):
        def decorator(f):
            self.bound.append((f, rule, options))
            return f

        return decorator
