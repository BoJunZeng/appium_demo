# -*- coding: UTF-8 -*-

import yaml
import sys
import os
from appium import webdriver

import logging.config

def appium_desired(udid, port):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    conf_path = os.path.join(root_dir, 'conf', 'desired_caps.yaml')
    print("desired caps conf path:%s" % conf_path)
    # conf_path = "../conf/desired_caps.yaml"
    desired_caps = {}

    # LOG_CONF = '../conf/log.conf'
    LOG_CONF = os.path.join(root_dir, 'conf', 'log.conf')
    print("logging conf path:%s" % LOG_CONF)
    logging.config.fileConfig(LOG_CONF)
    logger = logging.getLogger()

    # load desired config file
    with open(conf_path, "r", encoding="utf-8") as conf_file:
        desired_data = yaml.load(conf_file, Loader=yaml.FullLoader)

    desired_caps['platformName'] = desired_data['platformName']
    desired_caps['platformVersion'] = desired_data['platformVersion']
    desired_caps['deviceName'] = desired_data['deviceName']
    desired_caps['udid'] = udid
    desired_caps['appPackage'] = desired_data['appPackage']
    desired_caps['appActivity'] = desired_data['appActivity']
    desired_caps['unicodeKeyboard'] = desired_data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = desired_data['resetKeyboard']
    local_host = desired_data['host']
    # port = port

    print('http://' + str(local_host) + ':' + str(port) + '/wd/hub')
    driver = webdriver.Remote('http://' + str(local_host) + ':' + str(port) + '/wd/hub', desired_caps)
    logger.debug("INFO:start app...")

    # driver.implicitly_wait(2)
    return driver


def quit_driver(driver):
    driver.quit()

#
# if __name__ == '__main__':
#     appium_desired()






