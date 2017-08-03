#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from flask import Blueprint

home = Blueprint("home",
                 __name__,
                 # template_folder='templates',
                 # static_folder='static'
                 )

from . import views
