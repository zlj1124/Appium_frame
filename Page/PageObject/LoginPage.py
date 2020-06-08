'''
@Descripttion: 
@Author: zlj
@Date: 2020-06-03 15:24:37
'''
import time
from Page.BasePage import BasePage
from utils.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()

    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    
  
    def login(self, username, password):
        """登录流程"""
       
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

        
    
    def input_username(self, username):

    #    元组前面加*号传入python函数时，元组中的元素被解开作为独立的参数依次传给python函数，相当于解包a,b=(1,2)
        return self.send_keys(username,*LoginPage.username)

   
    def input_password(self, password):
        return self.send_keys(password,*LoginPage.password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)
    
    # def click_auth_but(self):
    #     return self.click(*)
  

if __name__ == "__main__":
    a=LoginPage()
    a.login('18323177363','18323177363')
