#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template("main/main.html")