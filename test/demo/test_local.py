# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_local.py
# Time       ：2022-05-06 16:34
# Author     ：author name
# version    ：python 3.7-32bit
# Description：使用local来实现线程隔离
"""
import threading
import time

from werkzeug.local import Local

local = Local()
local.value = 2


def worker():
    local.value = 1
    t = threading.current_thread()
    print(t.name + "===" + str(local.value), end="\n")
    time.sleep(1)


t1 = threading.Thread(target=worker)
t1.start()

print("main===" + str(local.value))
