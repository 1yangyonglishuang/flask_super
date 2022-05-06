# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : test_book.py
# Time       ：2022-05-06 19:04
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
import json
import unittest
from app.app import create_app

app = create_app()


class BookTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_book(self):
        response = app.test_client().get('/v1/book/get')
        json_data = response.data
        self.assertEqual(json_data.decode(), "get book")


if __name__ == '__main__':
    unittest.main()
