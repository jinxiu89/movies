#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from . import home
from flask import render_template, \
    redirect, url_for


@home.route('/login/')
def login():
    # todo::Post过来的数据，验证是否登陆
    return render_template('home/login.html')


@home.route('/logout/')
def logout():
    # todo::清除session
    return redirect(url_for('home.login'))


@home.route('/')
def index():
    # todo::查询列表，调出幻灯片，标签列出
    return render_template('home/index.html')


@home.route('/search/')
def search():
    # todo:查询功能
    return render_template('home/search.html')


@home.route('/play/')
def play():
    return render_template('home/play.html')


@home.route('/register/')
def register():
    return render_template('home/register.html')


@home.route('/user')
def user():
    return render_template('home/user.html')


@home.route('/user/pwd')
def pwd():
    return render_template('home/pwd.html')


@home.route('/moviecol/')
def moviecol():
    return render_template('/home/moviecol.html')


@home.route('/animation/')
def animation():
    return render_template('common/animation.html')
