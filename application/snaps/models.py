#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/3 下午9:24
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : models.py
@desc :
"""
import datetime
import hashlib
from application import db


def content_hash(context):
    content = context.current_parameters['content']
    created_on = context.current_parameters['created_on']
    return hashlib.sha1(content + str(created_on)).hexdigest()


class Snap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    extension = db.Column(db.String(15))
    content = db.Column(db.Text())
    hash_key = db.Column(db.String(40), unique=True, default=content_hash)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow(), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('snaps', lazy='dynamic'))

    def __repr__(self):
        return '< Snap {!r} >'.format(self.id)


if __name__ == '__main__':
    pass
