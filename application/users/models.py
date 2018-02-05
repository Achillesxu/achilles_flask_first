#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/3 下午1:41
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : models.py
@desc :
"""
import datetime
from sqlalchemy.ext.hybrid import hybrid_property

from application import db, flask_crypt


class User(db.Model):
    """
    model attribute class for user
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column('password', db.String(64))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, email, username, password):
        """Initialize the user object with the required attributes."""

        self.email = email
        self.username = username
        self.password = flask_crypt.generate_password_hash(password)
        self.created_on = datetime.datetime.utcnow()

    def __repr__(self):
        return '<User {!r}>'.format(self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anomyous(self):
        return False

    def get_id(self):
        return self.id

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = flask_crypt.generate_password_hash(password)


if __name__ == '__main__':
    pass
