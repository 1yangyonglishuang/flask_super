# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : book.py
# Time       ：2022-05-03 10:42
# Author     ：author name
# version    ：python 3.7-32bit
# Description：
"""
from flask import request

from app.libs.red_print import RedPrint
from app.models.base import db
from app.models.user import Article, User

api = RedPrint("book")


@api.route('/get/<int:book_id>')
def get_book(book_id):
    print(book_id, type(book_id))
    article = Article.query.filter(Article.id == book_id).first()
    article = dict(article)
    article['user'] = dict(article.user)
    return article


@api.route("/<int:user_id>")
def get_book_by_userid(user_id):
    # 外键属性
    # user = User.query.filter(User.id == user_id).first()
    # return {"msg": [dict(article) for article in user.articles]}
    data = db.session.query(User.nickname, Article.name).outer_join(User, User.id == Article.user_id).filter(
        User.id == Article.id).all()
    print(data)
    return "ok"


@api.route("/create", methods=["POST"])
def create_book():
    data = request.json
    print(data)
    with db.auto_commit():
        article = Article()
        article.name = data.get('name')
        article.price = data.get('price')
        article.count = data.get('count')
        article.user_id = data.get('user_id')
        db.session.add(article)
    return "create book"
