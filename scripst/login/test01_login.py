import requests
import unittest
import os
from ddt import ddt,data

import config
from common.handle_ddt import Ddt_data
from common.handel_log import new_login
from api.login import LoginAPI

login_data=Ddt_data(os.path.join(config.data_dir,'login_data.xlsx'),'login')
#构造数据
@ddt()
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

    #登录case
    @data(*login_data.all_data())
    def test01_login_success(self,case):
        new_login.warning('StartTest,Test_Case{}:'.format(case['case_name']), case)
        new_login.warning('TestData————》{}'.format(case),case)
        case['data'] =eval(case['data'])
        responese=self.loginapi.login(self.session,case['data'])
        self.assertEqual(case['code'],responese.json().get('code'))
        # self.assertEqual(msg, responese.json().get('msg'))
        config.Token=responese.json().get('data.token')

