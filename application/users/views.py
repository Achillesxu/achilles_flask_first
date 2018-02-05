#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/3 下午12:59
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : views.py
@desc :
"""
from flask import (Blueprint, flash, render_template, url_for, redirect, g)
from flask_login import login_user, logout_user, current_user
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from .models import User
from application import flask_crypt

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/me')
def users_me():
    return 'from blueprint users me', 200


class LoginForm(Form):
    """
    Represents the basic Login form elements & validators.
    """
    username = StringField('username', validators=[DataRequired(), ])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Basic user login functionality.
    If the user is already logged in , we redirect the user to the default snaps index page.
    If the user is not already logged in and we have form data that was submitted via POST request,
    we call the validate_on_submit() method of the Flask-WTF
    Form object to ensure that the POST data matches what
    we are expecting. If the data validates, we login the
    user given the form data that was provided and then
    redirect them to the default snaps index page.
    Note: Some of this may be simplified by moving the actual User
    loading and password checking into a custom Flask-WTF validator
    for the LoginForm, but we avoid that for the moment, here.
    """
    if hasattr(g, 'user') and g.user.is_authenticated():
        return redirect(url_for('snaps.listing'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if not user or not flask_crypt.check_password_hash(user.password, form.password.data):
            flash("No such user exists.")
            return render_template('users/login.html', form=form)
        login_user(user, remember=True)
        return redirect(url_for('snaps.listing'))
    return render_template('users/login.html', form=form)


@users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('snaps.listing'))


if __name__ == '__main__':
    pass
