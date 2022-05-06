# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_theads_isolation.py
# Time       ：2022-05-06 15:51
# Author     ：author name
# version    ：python 3.7-32bit
# Description：测试自定义线程隔离
"""

import threading
import time


# 未使用线程隔离


# class Request1:
#     a = 1
#
#
# response = Request1()
#
#
# def worker(value: int = None):
#     t = threading.current_thread()
#     if value:
#         Request1.a = value
#     print(f"未使用隔离的变量a:::{response.a}", end="\n")
#     time.sleep(1)
#
#
# f1 = threading.Thread(target=worker, args=[2], name="f1")
# f2 = threading.Thread(target=worker, name="f2")
#
# f1.start()
# f2.start()
#
# print("#" * 100)

class Request:
    a = 1


def worker(value: int = None):
    item = {}
    t = threading.current_thread()
    item.setdefault(t.name, Request())
    if value:
        item[t.name].a = value
    print(f"子线程中的变量a:::{item[t.name].a}", end="\n")

    time.sleep(1)
    print(item)


t1 = threading.Thread(target=worker, args=[2], name="t1")
t2 = threading.Thread(target=worker, name="t2")

t1.start()
t2.start()
