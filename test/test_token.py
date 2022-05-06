# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_token.py
# Time       ：2022-05-06 19:35
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import json
import unittest
from app.app import create_app

app = create_app()


class TokenTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_token(self):
        response = app.test_client().post(
            '/v1/token/',
            json={
                "account": "super@qq.com",
                "secret": "123456",
                "type": 100
            })

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
