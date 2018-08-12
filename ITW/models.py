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
    title = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(128), nullable=False, default='中国')
    pid = db.Column(db.String(20), nullable=False, default='None')
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
    tutorial_item = db.Column(db.String(128))
    need_invite = db.Column(db.String(10), nullable=False)
    excursion = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(10))
    birthday = db.Column(db.String(50))
    food_preference = db.Column(db.String(50), nullable=False)
    goto_talk = db.Column(db.String(10), nullable=False)

    total_fee = db.Column(db.Integer, nullable=False)
    

class Reservations(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    affiliation = db.Column(db.String(128), nullable=False)
    checkin_date = db.Column(db.String(50), nullable=False)
    checkout_date = db.Column(db.String(50), nullable=False)
    identity_num = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    

class Rooms(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    type_num = db.Column(db.Integer, nullable=False)
    type_name = db.Column(db.String(50), nullable=False)
    total_num = db.Column(db.Integer, nullable=False)
    available_num = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    in_date = db.Column(db.Integer, nullable=False)