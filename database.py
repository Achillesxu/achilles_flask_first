#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/5 下午4:06
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : database.py
@desc : yield database tables
"""
from application import db


if __name__ == '__main__':
    db.create_all()
