#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/1 上午10:07
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site :
@File : __init__.py
@desc :
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

# base64.b64encode(os.urandom(32))
app.config['SECRET_KEY'] = 'nc2mLtX9hpSV154w7G0okCDCArVFVLDnOmHgYKIWXSY='
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://achilles_psql:Filter1986@localhost/ac_psql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
flask_crypt = Bcrypt()

from application.users import models as user_models
from application.users.views import users
from application.snaps.views import snaps

app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(snaps, url_prefix='/snaps')


@login_manager.user_loader
def load_user(user_id):
    return user_models.User.query.get(int(user_id))
