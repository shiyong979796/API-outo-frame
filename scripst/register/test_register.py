#:@ TIME 2021/10/3   13:13
#:@FILE  test_register.py
#:@EMAIL  1557225637@QQ.COM
import unittest
from ddt import ddt,data
from api.register import Register
import config
import os
import random

from common.handel_log import new_log
from common.handle_ddt import Ddt_data
from common.handle_cf_file import Config_file
from common.handle_database import Database
from common.handel_replace_data import replace_data


new_register_data=Ddt_data(os.path.join(config.data_dir,'register.xlsx'),'register_form')#创建ddt对象
cf=Config_file(os.path.join(config.conifg_file_dir,'Data_base_cf.ini'))#文件配置对象
db=Database()
# @unittest.skip
@ddt()
class Test_register(unittest.TestCase):
    def setUp(self):
        self.new_Register=Register()


    def tearDown(self):
        pass

    # #注册成功
    @data(*new_register_data.all_data())
    def test_register(self,case):
        self._testMethodDoc = case['case_name']
        case=replace_data(case,''.join(random.sample('abcdefghijklmnopqrstuvwxyz',8)),'#data#')#读取 case字典内 字符穿替换成新
        case['data'] = eval(case['data'])

        result = self.new_Register.register(case['data'])  #调用注册接口
        new_log.warning('case_name：{}'.format(case['case_name']))#日志  用例名称
        new_log.warning('Expect_case_data：{}'.format(case))
        new_log.warning('Reslut_json_data：{}'.format(result.json()))

        try:
            self.assertEqual(result.json().get('code'),case['code'])
            self.assertEqual(result.json()['code'], case['code'])  #第二种code方式
            self.assertEqual(result.json().get('msg'),case['msg'])
            if case['check_sql']:
                new_log.debug('需要校验数据库')
        except AssertionError:
            new_log.debug("断言失败............................断言失败",AssertionError)
            raise

