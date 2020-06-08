# -*- encoding: utf-8 -*-
'''
@Descripttion: 
@Author: zlj
@Date: 2020-06-03 14:19:58
'''
import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from utils.read_caps import read_caps
import logging.config
from Config import conf

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WD #别名为WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path),'screenshots')
if not os.path.exists(screenshot_path):os.mkdir(screenshot_path)

logging.config.fileConfig(conf.LOG_CONFIG_LOCATION)
logger = logging.getLogger(__name__)


class BasePage(object):
    """Base封装公用的方法"""
  
    def __init__(self,driver,timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.timeout=timeout
        self.driver=driver
        print('basepage{}'.format(driver))
  

    def find_element(self, by, locator):
        """
        查找单个元素
        """
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.timeout).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        查找一组元素
        """
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.timeout).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements        



    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)    

    def send_keys(self, value, by,locator=''):
        """重写在文本框中输入内容的方法"""
        # print('info:input "{}"'.format(value))
        logger.info('info:input "{}"'.format(value))
        try:
            element= WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator)))
            element.send_keys(value)
      
        except AttributeError as e:
            print(e)

  
    def click(self, by, locator):
        """点击某个元素"""
        logger.info('info:click "{}"'.format(locator))
        # print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element!=None:
            element.click()
        else:
            print('the "{}" unclickable!')


    def is_click(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, 30). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                print("元素不可以点击")
            else:
                return element
        else:
            print('the "{}" error!'.format(by))


    def getScreenShot(self):
        """重写截图方法"""
        self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d'))
        self.driver.get_screenshot_as_file(self.sh_file)


    def get_windows_size(self):
        """获取屏幕大小"""
        windows_size = self.driver.get_window_size()
        return windows_size

    # 权限处理
    def click_shoot_windows(self,by,locator):
         try:

            els = self.find_elements(by, locator)
            for el in els:
                if el.text == u'允许':
                    self.driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
               
         except:
             print("无权限弹框处理")


    #action_touch只采用元素位置定位，不用坐标 
    #坐标弊端，不同分别率的坐标不一致
    def long_press(self,by,locator,time=2000):
        print('info:long_press "{}"'.format(locator))
        try:
            element = self.find_element(by, locator)
            TouchAction(self.driver).long_press(ele=element,duration=time).perform()
        except AttributeError as e:
            print(e)   
        

    
    def close_app(self):
        self.driver.quit()    

if __name__ == "__main__":
    pass
    
    




