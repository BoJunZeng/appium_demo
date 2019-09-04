# -*- coding: UTF-8 -*-
from baseView.BaseView import BaseView
from common.desired_caps import appium_desired
from appium import webdriver


class Common(BaseView):

    def __init__(self, driver):
        self.driver = driver





if __name__ == '__main__':
    driver = appium_desired()








