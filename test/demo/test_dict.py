# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_dict.py
# Time       ：2022-05-04 10:40
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import os


class Person(object):
    name = "blue"
    age = 18

    def __init__(self, gender):
        self.gender = gender

    def keys(self):
        return ("name", "age", "gender")

    def __getitem__(self, item):
        return getattr(self, item)

    # def __dict__(self):
    #     print({key: self.__getitem__(key) for key in self.keys()})
    #     return {key: self.__getitem__(key) for key in self.keys()}


person = Person("男")
print(person.__dict__)
print(dict(Person("女")))
# print("environment".upper())
# print(os.environ["ENVIRONMENT"])

