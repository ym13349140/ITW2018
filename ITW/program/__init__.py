#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
program = Blueprint('program', __name__)
from . import views
