#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-28 10:43:15
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-28 10:43:15
from flask import render_template
from app import app
from forms.edit_page import EditPages


@app.route(r'/')
@app.route(r'/index')
def index():
    pages = [{
        'page_name': '首页',
        'ele_name': '登录按钮',
        'ele_locater': 'Xpath',
        'ele_locater_value': r"span//div[.='test']"
    }, {
        'page_name': '首页',
        'ele_name': '登录按钮',
        'ele_locater': 'Xpath',
        'ele_locater_value': r"span//div[.='test']"
    }, {
        'page_name': '首页',
        'ele_name': '登录按钮',
        'ele_locater': 'Xpath',
        'ele_locater_value': r"span//div[.='test']"
    }]
    return render_template("index.html", title='主页', pages=pages)


@app.route(r'/page/editpage')
def edit_pages():
    form = EditPages()
    return render_template('edit_pages.html', title='编辑页面', form=form)
