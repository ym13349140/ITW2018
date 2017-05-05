#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import travel
from flask import render_template, jsonify, request


@travel.route('/travle/about_GuangZhou')
def index():
    return render_template("travel/main.html",
                           tab="travel",
                           tag="guangzhou")


@travel.route('/travle/about_SYSU')
def sysu():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='sysu')


@travel.route('/travle/Cantonese_Cuisine')
def food():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='food')


@travel.route('/travle/Visa_Information')
def visa():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='visa')


@travel.route('/travle/Hong_Kong')
def hongkong():
        return render_template("travel/main.html",
                               tab="travel",
                               tag='hongkong')
