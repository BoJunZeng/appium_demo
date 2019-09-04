# -*- coding: UTF-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

ID = "ID"
NAME = "NAME"
CLASS_NAME = "CLASS_NAME"
DESCRIPTION = "DESCRIPTION"
INDEX = "INDEX"
NETWORK_DICT = {"NO_CONNECTION": 0, "AIRPLANE_MODE": 1, "WIFI_ONLY": 2, "DATA_ONLY": 4, "ALL_NETWORK_ON": 6}


class BaseView(object):

    def __init__(self, driver):
        self.driver = driver

    def delay(self, second):
        time.sleep(second)

    def __get_xpath_feature_part(self, loc):
        args = [item.strip() for item in loc.split(",")]
        key_index = 0
        value_index = 1
        if len(args) == 2:
            xpath_feature = "contains(@" + args[key_index] + ", '" + args[value_index] + "')"
        elif len(args) == 3:
            # args[2] == 1 means use clear xpath search
            if args[2] == "1":
                xpath_feature = "@" + args[key_index] + "='" + args[value_index] + "'"
            else:
                xpath_feature = "contains(@" + args[key_index] + ", '" + args[value_index] + "')"
        return xpath_feature + " and "

    def __make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""
        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            feature = self.__get_xpath_feature_part(loc)
        else:
            for sub_loc in loc:
                feature += self.__get_xpath_feature_part(sub_loc)
        feature = feature.rstrip(" and ")
        return feature_start + feature + feature_end

    def find_element(self, args):
        _by = args[0]
        _value = args[1]
        if _by == By.XPATH:
            _value = self.__make_xpath_with_feature(_value)
            print(_value)
        return WebDriverWait(self.driver, 5, 1).until(lambda f: f.find_element(_by, _value))

    def find_element_by_text(self, _text):
        if _text in self.driver.page_source:
            uiautomator_str = "new UiSelector().text(\"" + _text + "\")"
        else:
            uiautomator_str = "new UiScrollable(new UiSelector().scrollable(true))\
                .scrollIntoView(new UiSelector().text(\"" + _text + "\"))"
        return self.driver.find_element_by_android_uiautomator(uiautomator_str)

    def find_element_by_desc(self, _desc):
        if _desc in self.driver.page_source:
            uiautomator_str = "new UiSelector().description(\"" + _desc + "\")"
        else:
            uiautomator_str = "new UiScrollable(new UiSelector().scrollable(true))\
                .scrollIntoView(new UiSelector().description(\"" + _desc + "\"))"
        return self.driver.find_element_by_android_uiautomator(uiautomator_str)

    def get_toast(self, toast, timeout=10):
        xpath = '//*[contains(@text, \'{}\')]'.format(toast)
        toast_ele = WebDriverWait(self.driver, timeout).until(lambda func: func.find_element_by_xpath(xpath))
        return toast_ele.text

    def check_toast_exists(self, toast, timeout=10):
        xpath = '//*[contains(@text, \'{}\')]'.format(toast)
        toast_ele = WebDriverWait(self.driver, timeout).until(lambda func: func.find_element_by_xpath(xpath))
        if toast in toast_ele.text:
            return True
        else:
            return False

    def get_element_bounds(self, element):
        ele_bounds = {}
        lt_pos = element.location
        ele_size = element.size
        ele_bounds['top'] = lt_pos['y']
        ele_bounds['left'] = lt_pos['x']
        ele_bounds['bottom'] = lt_pos['y'] + ele_size['height']
        ele_bounds['right'] = lt_pos['x'] + ele_size['width']
        return ele_bounds

    def get_network_connection_type(self):
        network_code = self.driver.network_connection
        if network_code in NETWORK_DICT.values():
            return list(NETWORK_DICT.keys())[list(NETWORK_DICT.values()).index(network_code)]

    def scoll_to(self, _type, _content):
        _type = None
        if _type == ID:
            uiautomator_str = ""



