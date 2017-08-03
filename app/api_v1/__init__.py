#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from flask import Blueprint

api_v1 = Blueprint("api_v1",
                   __name__,
                   template_folder='templates',
                   static_folder='static'
                   )
import app.api_v1.views
