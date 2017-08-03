#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from flask import Flask, render_template
from app.home import home
from app.admin import admin
from app.api_v1 import api_v1

app = Flask(__name__)
app.debug = True
app.register_blueprint(home)
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(api_v1, url_prefix="/api_v1")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('common/404.html'), 404
