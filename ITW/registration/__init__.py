#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
registration = Blueprint('registration', __name__)
from . import views
