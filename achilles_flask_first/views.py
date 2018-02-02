#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : achilles_flask_first
@Time : 2018/2/1 上午11:39
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : views.py
@desc :
"""
from achilles_flask_first import app


@app.route('/')
def hello():
    return 'hello, world!'


if __name__ == '__main__':
    pass
