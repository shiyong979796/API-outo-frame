import requests
from config import HEADER
import config
#创建类
class LoginAPI:
    #初始化url
    def __init__(self):
        self.url_login='{}/1.0/user/login'.format(config.PROD_URL)
        self.url_showroom="{}/1.0/showroom".format(config.PROD_URL)



    def login(self,session,login_data):#定义api调用后返回参数接口（参数未赋值  断言处赋值 ，get字段做断言）
        return session.post(self.url_login,json=login_data,headers=HEADER)#调用方法=调用接口，参数化传入 login_data,headers=HEADER



