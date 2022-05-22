# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : article.py
# Time       ：2022-05-22 17:00
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base, db


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    price = Column(Integer, default=20)
    count = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = db.relationship("User", backref=db.backref("articles"))

    def keys(self):
        return ["id", "name", "price", "count", "user_id"]
