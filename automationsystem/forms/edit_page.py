#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-28 14:10:21
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-28 14:10:21
from flask_wtf import Form
from wtforms import TextField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class EditPages(Form):
    choices = [('ID', 'ID'), ('Xpath', 'Xpath'), ('name', 'NAME'),
               ('css', 'CSS'), ('Text', 'TEXT'), ('Link', 'LINK')]
    pagename = StringField('页面名称:', validators=[DataRequired()])
    elename = StringField('元素名称:', validators=[DataRequired()])
    ele_locater_type = SelectField('元素定位类型:', choices=choices)
    ele_locater_value = StringField('元素定位的值:', validators=[DataRequired()])
    submit = SubmitField('保存')
