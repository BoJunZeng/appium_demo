# -*- coding: UTF-8 -*-

from appium import webdriver
import sys
import os
import yaml
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import common.desired_caps as dc
import time
from base.BaseView import BaseView
import logging
from utils.appium_utils import AppiumUtils
from common.common_adb import AdbCommon
from threading import Thread

# conf_file = os.path.join(sys.path[0], 'conf', 'desired_caps.yaml')
# print("conf_file:%s" % conf_file)
#
# with open(conf_file, "r") as f:
#     desired_data = yaml.load(f, Loader=yaml.FullLoader)
#
# desired_caps = {}
#
# desired_caps['platformName'] = desired_data['platformName']
# desired_caps['platformVersion'] = desired_data['platformVersion']
# desired_caps['deviceName'] = desired_data['deviceName']
# desired_caps['udid'] = desired_data['udid']
#
# # desired_caps['app'] = os.path.join(sys.path[0], 'resource', 'app', 'gallery.apk')
# # desired_caps['appPackage'] = 'com.tclhz.gallery'
# # desired_caps['appActivity'] = 'com.tcl.gallery.app.GalleryActivity'
# desired_caps['appPackage'] = desired_data['appPackage']
# desired_caps['appActivity'] = desired_data['appActivity']
#
# desired_caps['unicodeKeyboard'] = desired_data['unicodeKeyboard']
# desired_caps['resetKeyboard'] = desired_data['resetKeyboard']
#
#
# local_host = desired_data['host']
# port = desired_data['port']
#
# print('http://' + str(local_host) + ':' + str(port) + '/wd/hub')
#
# driver = webdriver.Remote('http://' + str(local_host) + ':' + str(port) + '/wd/hub', desired_caps)
# au = au.AppiumUtils(driver)
#
# dsplay_view = au.find_element_by_text('Display')
# try:
#     WebDriverWait(driver, 10).until(lambda func: func.find_element_by_android_uiautomator("new UiSelector().text(\"Display\")"))
# except NoSuchElementException:
#     print("NOT exists")
# else:
#     dsplay_view.click()

# print(ft_size)
# ft_size.click()

if __name__ == '__main__':
    _host = '127.0.0.1'
    _port = 4723
    AppiumUtils().start_appium_server(_host, _port)
    ADB = AdbCommon()
    driver = dc.appium_desired(udid='1649c2e3', port=_port)
    bv = BaseView(driver)
    time.sleep(2)
    # SEARCH_BTN = (By.XPATH, "//*[@text='Display']")
    SEARCH_BTN = (By.XPATH, "text, Display, 1")
    # SEARCH_BTN = (By.XPATH, ["text, Display", "index, 0, 1"])
    # print(time.strftime("%Y-%m-%D %H:%M:%S"))
    # SEARCH_BTN = (By.NAME, "Search settings")
    search_view = bv.find_element(SEARCH_BTN)
    search_view.click()
    time.sleep(3)
    # search = bv.find_element_by_desc(_desc='Search settings')
    # ele_bounds = bv.get_element_bounds(search)
    # print(ele_bounds)
    # bv.delay(5)
    # print(bv.get_network_connection_type())
    # TouchAction(driver).move_to()
    # ele = driver.find_element_by_xpath("//*[@text='Apps']/parent::android.widget.LinearLayout/preceding-sibling::android.widget.ImageView")
    # # print(ele.text)
    # ele.click()
    # toast = bv.get_toast(toast='App does not')
    dc.quit_driver(driver)
    # ADB.open_app(packageName='com.tclhz.gallery', activity='com.tcl.gallery.app.GalleryActivity')
    # time.sleep(2)

    # logging.info("==========press home key==========")
    # driver.keyevent(3)
    #
    # pid = AppiumUtils().get_netstat_pid_by_port(_port)
    # print("pid:%d" % pid)
    # AdbCommon().call_adb("reboot")
    # print("----i was reboot ----")
    # time.sleep(120)
    # print("start done!")
    # l_devices = AdbCommon().attach_devices()
    # for device in l_devices:
    #     print(device)
    # cmd = "netstat -nlptu | awk '{print $4,$7}' | grep " + str(_port)
    # shell_dict = shell_cmd(cmd)
    # rc = shell_dict['returncode']
    # std_out = shell_dict['std_out']
    # if rc == 0:
    #     print(std_out)
    #     for line in std_out.split('\n'):
    #         print("--->%s" % line)
        # if ":" + str(_port) in std_out:
        #     print(std_out)
        #     if ":" + str(_port) in line:
        #         print("----find----")
        #         print(line.split(' ')[1])
        #     else:
        #         print("----not find----")
    # gv = driver.find_element_by_id("")
    # gv.click()



