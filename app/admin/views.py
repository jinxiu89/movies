#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from . import admin


@admin.route('/')
def index():
    return "hello admin!"
