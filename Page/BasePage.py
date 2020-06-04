# -*- encoding: utf-8 -*-
'''
@Descripttion: 
@Author: zlj
@Date: 2020-06-03 14:19:58
'''
import os
import time
import sys
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils.read_caps import read_caps
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

class BasePage(object):
    """Base封装公用的方法"""
  
    def __init__(self,timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.timeout=timeout
        data = read_caps()
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noSign'] = data['noSign']
        desired_caps['noReset'] = data['noReset']
        desired_caps['unicodeKeyboard']=True #中文显示
        desired_caps['resetKeyboard']=True
        self.driver = webdriver.Remote('http://' + data['ip'] + ':' + str(data['port']) + '/wd/hub',desired_caps)
      





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

    # def clear_key(self,loc):
    #     """重写清空文本输入法"""
    #     time.sleep(3)
    #     self.find_element(loc).clear()

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        print('by:{}locator:{}'.format(by,locator))


        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)    

    def send_keys(self, value, by,locator=''):
        """重写在文本框中输入内容的方法"""
        print("locator:{},by:{}".format(locator,by))
        print('info:input "{}"'.format(value))
        self.clear_key(locator)
        try:
            element= WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((by, locator)))
            element.send_keys(value)
            time.sleep(1)
        except AttributeError as e:
            print(e)

  
    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
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
    
    def close_app(self):
        self.driver.quit()    

if __name__ == "__main__":
    test= Action()
    
    




