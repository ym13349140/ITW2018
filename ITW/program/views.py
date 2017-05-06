#! /usr/bin/env python
# -*- coding: utf-8 -*-
from . import program
from flask import render_template, jsonify, request


@program.route('/glance')
def glance():
    return render_template("program/main.html",
                           tab="program",
                           tag="glance")


@program.route('/full_program')
def full_program():
    return render_template("program/main.html",
                           tab="program",
                           tag="full_program")


@program.route('/invited_papers')
def invited_papers():
    return render_template("program/main.html",
                           tab="program",
                           tag="invited_papers")


@program.route('/tutorial_call')
def tutorial_call():
    return render_template("program/main.html",
                           tab="program",
                           tag="tutorial_call")


@program.route('/social_events')
def social_events():
    return render_template("program/main.html",
                           tab="program",
                           tag="social_events")
