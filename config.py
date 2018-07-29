#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_SSL = True

    MAIL_USERNAME = 'itw2018gz@gmail.com'
    MAIL_PASSWORD = 'jux3129ha'

    # MAIL_USERNAME = 'ym13349140@gmail.com'
    # MAIL_PASSWORD = '310810woainimin'

     
    # MAIL_SERVER = 'smtp.qq.com'
    # MAIL_USE_SSL = True

    # MAIL_USERNAME = '1697937077@qq.com'
    # MAIL_PASSWORD = 'invgarinouiofegg'

    MAIL_SUBJECT_PREFIX = 'ITW2018-Registration Successfully'


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    def __init__(self):
        pass

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql+pymysql://root:ITW#2018itw@localhost/itw2018')


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
