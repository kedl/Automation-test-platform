#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-24 20:46:07
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-24 20:46:07
import logging

logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)


def logger(func):
    def wrapper():
        logging.info("LOG INFO: Begin to execute function: %s" % func.__name__)
        logging.info("LOG INFO: Finish executing function: %s" % func.__name__)

    return wrapper
