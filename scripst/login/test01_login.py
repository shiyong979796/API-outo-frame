import json
import requests
import unittest
from parameterized import parameterized
# from config import base_dir
import config
from api.login import LoginAPI

#构造数据
def build_data(): #创建参数方法
    file=config.base_dir+'/data/login_data/login_data.json'  #获取参数文件路径
    test_data=[]
    with open(file,encoding='utf-8') as f: #打开文件 open方法 传入 路径，wb  写 二进制
        json_data=json.load(f) #加载json文件
    for  case_data in  json_data:
        login_data=case_data.get('login_data')
        code=case_data.get('code')
        msg=case_data.get('msg')
        case_name=case_data.get('case_name')
        test_data.append((login_data,code,msg,case_name))
    print(test_data)
    return test_data

class Test_login(unittest.TestCase):
    #前置方法
    def setUp(self):
        self.loginapi=LoginAPI()#实例化login接口类
        self.session=requests.session()#创建session对象

    #后置方法
    def tearDown(self):
        #关闭session对象
        if self.session:
            self.session.close()

    #登录成功
    @parameterized.expand(build_data())#引用参数化
    def test01_login_success(self,login_data,code,msg,case_name):
        print(case_name)
        responese=self.loginapi.login(self.session,login_data)
        self.assertEqual(code,responese.json().get('code'))
        self.assertEqual(msg, responese.json().get('msg'))
        config.Token=responese.json().get('data.token')