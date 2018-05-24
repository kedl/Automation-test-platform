#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-23 20:28:27
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-23 20:28:27
from selenium import webdriver
from logger.logger import logger


class DriverConf(object):
    """
    """

    @classmethod
    @logger
    def getbrowser(cls, browser):
        """
        """
        if isinstance(browser, str):
            browser = browser.lower()
            if browser == 'chrome':
                return webdriver.Chrome()
            elif browser == 'ie':
                return webdriver.Ie()
            elif browser == 'firefox':
                return webdriver.Firefox()
            else:
                raise NameError(
                    "Not found this browser,You can enter 'firefox', 'chrome' or 'ie'."
                )
        else:
            raise RuntimeError("Browser name must be string.")
