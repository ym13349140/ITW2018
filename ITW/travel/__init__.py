#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
travel = Blueprint('travel', __name__)
from . import views
