#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from . import api_v1


@api_v1.route('/')
def index():
    return "hello api_v1!"
