'''
@Descripttion: 
@Author: zlj
@Date: 2019-12-05 11:05:13
'''

import pytest
from Page.PageObject.LoginPage import LoginPage
from utils.parseConFile import ParseConFile


do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
userName = do_conf.get_locators_or_account('LoginAccount', 'username')
passWord = do_conf.get_locators_or_account('LoginAccount', 'password')


@pytest.fixture(scope='class')
def ini_pages(driver):#调用conftest.py中driver()获得全局_driver
  
    login_page = LoginPage(driver)
    # yield生成器实例化pageobject
    yield driver, login_page, 


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    yield login_page
    # driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page= ini_pages
    login_page.login(userName, passWord)
    yield login_page
    # driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()
