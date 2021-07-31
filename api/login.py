import requests
from config import HEADER
#创建类
class LoginAPI:
    #初始化url
    def __init__(self):
        self.url_login='https://apix.azazie.com/1.0/user/login'
        self.url_showroom="https://apix.azazie.com/1.0/showroom"



    def login(self,session,login_data):#定义api调用后返回参数接口（参数未赋值  断言处赋值 ，get字段做断言）
        # data={
        #     "email":email,
        #     "password":password
        # }
        return session.post(self.url_login,json=login_data,headers=HEADER)#调用方法=调用接口，参数化传入 login_data,headers=HEADER



