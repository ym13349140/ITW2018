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
