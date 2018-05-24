#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-24 20:08:30
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-24 20:08:30
import platform
import sys, os
sys.path.append(os.getcwd())
from logger.logger import logger


@logger
def get_system():
    """
    """
    return platform.system()
