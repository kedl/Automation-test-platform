#!/usr/local/bin/pyenv/python
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-28 10:42:11
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-28 10:42:11
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
import inspect

app = Flask(__name__)
app.config.from_object('config')
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)
nav = Nav()
nav.register_element('top',
                     Navbar(
                         u'AutomationSystem',
                         View(u'主页', 'index'),
                         View(u'页面管理', 'index'),
                         View(u'模块管理', 'index'),
                         View(u'计划管理', 'index'),
                         View(u'用例管理', 'index'),
                         View(u'数据管理', 'index'),
                         View(u'查看报告', 'index'),
                         Subgroup(
                             u'项目',
                             View(u'项目一', 'index'),
                             Separator(),
                             View(u'项目二', 'index'), ), ))
nav.init_app(app)
from app import views