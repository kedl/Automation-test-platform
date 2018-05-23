#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-23 22:23:40
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-23 22:23:40
import pytest
from Conf import host_conf


def test_key_not_in_dict():
    env = 'test'
    assert host_conf.getHost(env) is None


def test_key_is_not_string():
    env = 123
    assert host_conf.getHost(env) is None


def test_key_is_in_dict():
    env = 'QA'
    assert host_conf.getHost(env) is not None


def test_fuc_can_upper_string():
    env = 'uat'
    assert host_conf.getHost(env) is not None