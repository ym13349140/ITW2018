#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import travel
from flask import render_template, jsonify, request


@travel.route('/travel/about_GuangZhou')
def index():
    return render_template("travel/main.html",
                           tab="travel",
                           tag="guangzhou")


@travel.route('/travel/about_SYSU')
def sysu():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='sysu')


@travel.route('/travel/Visa_Information')
def visa():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='visa')


@travel.route('/travel/Hong_Kong')
def hongkong():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='hongkong')
