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
                         Subgroup(
                             u'页面管理',
                             View(u'查看页面', 'pages'),
                             Separator(),
                             View(u'添加页面', 'edit_pages'), ),
                         Subgroup(
                             u'模块管理',
                             View(u'查看模块', 'index'),
                             Separator(),
                             View(u'添加模块', 'index'), ),
                         View(u'计划管理', 'index'),
                         View(u'用例管理', 'index'),
                         View(u'数据管理', 'index'),
                         View(u'查看报告', 'index'), ))
nav.init_app(app)
from app import views