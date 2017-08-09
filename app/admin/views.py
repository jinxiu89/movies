#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from . import admin
from flask import render_template, url_for, redirect


@admin.route('/')
def index():
    return render_template('admin/base.html')


@admin.route('/login')
def login():
    return render_template('admin/login.html')


@admin.route('/logout')
def logout():
    return redirect(url_for('admin.login'))
