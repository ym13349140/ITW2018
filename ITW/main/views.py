#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template, jsonify, request


@main.route('/')
def index():
    return render_template("main/main.html",
                           tab="home")


@main.route('/committee')
def committee():
        return render_template("main/main.html",
                               tab='committee')


@main.route('/papers')
def papers():
        return render_template("main/main.html",
                               tab='papers')


@main.route('/venue')
def venue():
        return render_template("main/main.html",
                               tab='venue')


@main.route('/show_driver')
def show_driver():
        return render_template("venue/show_driver.html")


@main.route('/registration')
def registration():
        return render_template("main/main.html",
                               tab='registration')


@main.route('/accommodation')
def accommodation():
        return render_template("main/main.html",
                               tab='accommodation')
