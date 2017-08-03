#!/usr/bin/env python
# coding:utf-8
# author:jinxiu89@163.com
# create by thomas on 17-7-29.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Wavlink@163@localhost/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    """
    id:自增ID
    name:
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(2555), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))
    userlog = db.relationship("UserLog", backref='user')
    comment = db.relationship("Comment", backref='user')
    moviecol = db.relationship("MovieCol", backref="user")

    def __repr__(self):
        return '<name %r>' % self.name


class UserLog(db.Model):
    __tablename__ = "user_log"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<userlog %r>" % self.id


class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))
    movie = db.relationship("Movie", backref='tag')

    def __repr__(self):
        return "<Tag %r>" % self.name


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    keywords = db.Column(db.String(32))
    meta = db.Column(db.String(64))
    description = db.Column(db.String(128))
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger)
    commentnum = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    comment = db.relationship("Comment", backref='movie')
    moviecol = db.relationship("MovieCol", backref="movie")
    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Movie %r>" % self.title


class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    logo = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Preview %r>" % self.title


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Comment %r>" % self.id


class MovieCol(db.Model):
    __tablename__ = "movie_col"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Movie_col %r>" % self.id


class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    url = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Auth %r>" % self.name


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    auth = db.Column(db.String(255))
    admin = db.relationship("Admin", backref="role")
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Role %r>" % self.name


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    admin_log = db.relationship("AdminLog", backref="admin")
    action_log = db.relationship("ActionLog", backref="admin")
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M", time.localtime()))

    def __repr__(self):
        return "<Admin %r>" % self.name


class AdminLog(db.Model):
    __tablename__ = "admin_log"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M"))

    def __repr__(self):
        return "<Adminlog %r>" % self.id


class ActionLog(db.Model):
    __tablename__ = "action_log"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=time.strftime("%Y-%m-%d %H:%M"))

    def __repr__(self):
        return "<ActionLog %r>" % self.id


if __name__ == "__main__":
    db.create_all()
