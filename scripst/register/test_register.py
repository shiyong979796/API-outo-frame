#:@ TIME 2021/10/3   13:13
#:@FILE  test_register.py
#:@EMAIL  1557225637@QQ.COM
import unittest
from ddt import ddt,data
from api.register import Register
import config
import os
import random

from common.handel_log import new_login
from common.handle_ddt import Ddt_data
from common.handle_cf_file import Config_file
from common.handle_database import Database


new_register_data=Ddt_data(os.path.join(config.data_dir,'register.xlsx'),'register_form')#创建ddt对象
cf=Config_file(os.path.join(config.conifg_file_dir,'Data_base_cf.ini'))#文件配置对象
db=Database()

@ddt()
class Test_register(unittest.TestCase):
    def setUp(self):
        self.new_Register=Register()


    def tearDown(self):
        pass

    # #注册成功
    @data(*new_register_data.all_data())
    def test_register(self,case):
        case['data'] = eval(case['data'])
        if case['case_name']=='注册成功':
            data=case['data']['email']
            case['data']['email']=data+str(random.randint(30,10000000))
        result = self.new_Register.register(case['data'])  #调用注册接口
        new_login.warning('case_name：{}'.format(case['case_name']))#日志  用例名称
        new_login.warning('Expect_case_data：{}'.format(case))
        new_login.warning('Reslut_json_data：{}'.format(result.json()))

        try:
            self.assertEqual(result.json().get('code'),case['code'])
            self.assertEqual(result.json()['code'], case['code'])  #第二种code方式
            self.assertEqual(result.json().get('msg'),case['msg'])
            if case['check_sql']:
                new_login.debug('需要校验数据库')
        except AssertionError:
            new_login.debug("断言失败............................断言失败",AssertionError)
            raise

