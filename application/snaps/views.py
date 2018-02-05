#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2017, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : application
@Time : 2018/2/3 下午10:06
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : views.py
@desc :
"""
from flask import Blueprint, render_template, url_for, redirect, current_app, flash
from flask_login import login_required, current_user
from flask_wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired
from sqlalchemy import exc

from .models import Snap
from application import db

snaps = Blueprint('snaps', __name__, template_folder='templates')


class SnapForm(Form):
    name = StringField('name', validators=[DataRequired(), ])
    extension = StringField('extension', validators=[DataRequired(), ])
    content = StringField('content', widget=TextArea(), validators=[DataRequired(), ])


@snaps.route('/', methods=['GET', ])
def listing():
    """list all snaps, most recent first"""
    snaps = Snap.query.order_by(Snap.created_on.desc()).limit(20).all()
    return render_template('snaps/index.html', snaps=snaps)


@snaps.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    """add a new snap"""
    form = SnapForm()

    if form.validate_on_submit():
        user_id = current_user.id

        snap = Snap(user_id=user_id, name=form.name.data, extension=form.extension.data, content=form.content.data)
        db.session.add(snap)
        try:
            db.session.commit()
        except exc.SQLAlchemyError:
            current_app.exception('could not save the snap!')
            flash('something went wrong while posting the snap')
        else:
            return render_template('snaps/add.html', form=form)
    return redirect(url_for('snaps.listing'))


if __name__ == '__main__':
    pass
