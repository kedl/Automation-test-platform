#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-23 20:20:43
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-23 20:20:43
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class ElementBase(object):
    """
    """

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            self.driver = kwargs.get("driver")
            self.uri = kwargs.get("uri")
            self._type = kwargs.get("_type")
            self.host = kwargs.get("host")
            self.httpmethod = kwargs.get("httpmethod")
            self._value = kwargs.get("_value")
            self.kind = kwargs.get("kind")
            self.time = kwargs.get("time")

    def open_site(self):
        """
        """
        try:
            if self.httpmethod.lower() == 'https':
                self.driver.get("https://" + self.host + r"/" + self.uri)
            else:
                self.driver.get("http://" + self.host + r"/" + self.uri)
        except Exception as e:
            return e

    def find_element(self):
        """
        """
        try:
            element = WebDriverWait(self.driver, self.time).until(
                lambda driver: driver.find_element(by=self._type, value=self._value))
            return element
        except NoSuchElementException as e:
            return e.format()

    def find_elements(self):
        """
        """
        try:
            elements = WebDriverWait(self.driver, self.time).until(
                lambda driver: driver.find_elements(by=self._type, value=self._value))
            return elements
        except NoSuchElementException as e:
            return e.format()

    def existed(self):
        """
        """
        if self.kind.lower() == 'single':
            if self.find_element(self._type, self._value,
                                 self.time).is_displayed():
                return True
            else:
                return False
        elif self.kind.lower() == 'multiple':
            if self.find_elements(self._type, self._value,
                                  self.time).is_displayed():
                return True
            else:
                return False
        else:
            raise NameError(
                "This kind is not supported. Can only use 'single' or 'multiple'."
            )

    def selected(self):
        """
        """
        if self.kind.lower() == 'single':
            if self.find_element(self._type, self._value,
                                 self.time).is_selected():
                return True
            else:
                return False
        elif self.kind.lower() == 'multiple':
            if self.find_elements(self._type, self._value,
                                  self.time).is_selected():
                return True
            else:
                return False
        else:
            raise NameError(
                "This kind is not supported. Can only use 'single' or 'multiple'."
            )

    def wait_element_present(self):
        """"""
        if self.existed:
            return True
        else:
            return False
