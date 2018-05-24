#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Author: Danny
# @Date: 2018-05-23 20:20:43
# @Last Modified by:   Danny
# @Last Modified time: 2018-05-23 20:20:43
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from logger.logger import logger


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

    @logger
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

    @logger
    def find_element(self):
        """
        """
        try:
            element = WebDriverWait(self.driver, self.time).until(
                lambda driver: driver.find_element(by=self._type, value=self._value))
            return element
        except NoSuchElementException as e:
            return e.format()

    @logger
    def find_elements(self):
        """
        """
        try:
            elements = WebDriverWait(self.driver, self.time).until(
                lambda driver: driver.find_elements(by=self._type, value=self._value))
            return elements
        except NoSuchElementException as e:
            return e.format()

    @logger
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

    @logger
    def selected(self):
        """
        Returns whether the element is selected.
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

    # def wait_element_present(self):
    #     """"""
    #     if self.existed:
    #         return True
    #     else:
    #         return False

    @logger
    def mouse_hover(self):
        """
        Move to the specified element.
        """
        if self.existed:
            try:
                AC(self.driver).move_to_element(self.find_element).perform()
            except NoSuchElementException as e:
                return e.format()

    @logger
    def click(self):
        """
        """
        if self.enabled:
            self.find_element.click()

    # def get_text(self):
    #     """
    #     """
    #     if self.existed:
    #         return self.find_element.text

    @logger
    def isenabled(self):
        """
        """
        if self.existed:
            return self.find_element.is_enabled()

    @logger
    def get_property(self, name):
        """
        Gets the given property of the element.
        """
        if self.existed:
            return self.find_element.get_property(name)

    @logger
    def send_keys(self, text):
        """
        Simulates typing into the element
        """
        if self.existed:
            try:
                self.find_element.send_keys(text)
            except Exception as e:
                return e.format()

    @logger
    def send_keycode(self, keycode):
        """
        """
        function_map = {
            "Control": Keys.CONTROL,
            "Command": Keys.COMMAND,
            "Alt": Keys.ALT,
            "Shift": Keys.SHIFT,
            "Space": Keys.SPACE,
            "Esc": Keys.ESCAPE,
            "Tab": Keys.TAB,
            "BackSpace": Keys.BACK_SPACE,
            "Enter": Keys.ENTER,
            "Delete": Keys.DELETE
        }
        if self.existed:
            try:
                self.find_element.send_keys(function_map.get(keycode))
            except NameError:
                raise "Error, function is not defined"

    @logger
    def mock_keyboard(self, keycode, keyword):
        """
        """
        function_map = {
            "Control": Keys.CONTROL,
            "Command": Keys.COMMAND,
            "Alt": Keys.ALT,
            "Shift": Keys.SHIFT,
            "Space": Keys.SPACE,
            "Esc": Keys.ESCAPE,
            "Tab": Keys.TAB,
            "BackSpace": Keys.BACK_SPACE,
            "Enter": Keys.ENTER,
            "Delete": Keys.DELETE
        }
        if self.existed:
            try:
                AC(self.driver).key_down(function_map.get(keycode)).send_keys(
                    keyword).key_up(function_map.get(keycode)).perform()
            except Exception as e:
                return e.format()
