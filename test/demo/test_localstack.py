# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_localstack.py
# Time       ：2022-05-06 17:41
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import threading
import time

from werkzeug.local import LocalStack

local = LocalStack()
local.push(111)


def worker():
    local.push(222)
    t = threading.current_thread()
    print(t.name + "===" + str(local.top), end="\n")
    time.sleep(1)


t1 = threading.Thread(target=worker)
t1.start()
print()
print("main===" + str(local.top))