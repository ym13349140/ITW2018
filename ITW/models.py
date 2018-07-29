#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-09-19 23:06:09
from datetime import datetime
from flask import current_app
from . import db

""" 用户管理模块 """


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    random_id = db.Column(db.String(10), nullable=False)
    cname = db.Column(db.String(50))
    ename = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(128), nullable=False, default='中国')
    pid = db.Column(db.String(20), nullable=False)
    affiliation = db.Column(db.String(128), nullable=False)
    edas1 = db.Column(db.String(256))
    edas2 = db.Column(db.String(256))
    edas3 = db.Column(db.String(256))
    receipt = db.Column(db.String(10))
    receipt_title = db.Column(db.String(128))
    receipt_id = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    vip_num = db.Column(db.String(50))
    reg_type = db.Column(db.String(128), nullable=False)
    tutorial = db.Column(db.String(10), nullable=False)
    tutorial_item = db.Column(db.String(50))
    need_invite = db.Column(db.String(10), nullable=False)
    excursion = db.Column(db.String(128), nullable=False)
    food_preference = db.Column(db.String(50), nullable=False)
    goto_talk = db.Column(db.String(10), nullable=False)

    total_fee = db.Column(db.Integer, nullable=False)