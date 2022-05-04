# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : base.py
# Time       ：2022-05-03 12:49
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger
from contextlib import contextmanager

from app.libs.api_exceptions.exceptions import NotFundException


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404_for_api(self, ident, description=None):
        rv = self.get(ident)
        if rv is None:
            raise NotFundException()
        return rv

    def first_or_404_for_api(self, description=None):
        rv = self.first()
        if rv is None:
            raise NotFundException()
        return rv



db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def __getitem__(self, key):
        return getattr(self, key)




