#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
accommodation = Blueprint('accommodation', __name__)
from . import views
