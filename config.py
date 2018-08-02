#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    # MAIL_SERVER = 'smtp.163.com'
    # MAIL_USERNAME = 'maize_yang@163.com'
    # MAIL_PASSWORD = '310810woainiMIN'
    
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '1697937077@qq.com'
    MAIL_PASSWORD = 'nrzkfekrpzxidfie'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql+pymysql://itw2018:ITW#2018itw@localhost/itw2018')


class ProductionConfig(Config):
    def __init__(self):
        pass

    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql+pymysql://itw2018:ITW#2018itw@localhost/itw2018')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
