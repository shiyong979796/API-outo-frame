import requests
import unittest
import os
import json
from jsonpath import jsonpath
from ddt import ddt,data

import path
from common.handle_excel import Excel_data
from common.handle_log import new_log
from common.handle_request import send_request

login_data=Excel_data(os.path.join(path.excel_dir, 'excel_data.xlsx'), 'login')
#构造数据
# @unittest.skip
@ddt()
class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        new_log.info("======  登录模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        new_log.info("======  登录模块用例 执行结束  ========")


    #前置方法
    def setUp(self):
        pass

    #后置方法
    def tearDown(self):
        pass

    #登录case
    @data(*login_data.all_data())
    def test01_login_success(self,case):
        new_log.info("*********   执行用例{}：{}   *********".format(case["id"], case["case_name"]))
        self._testMethodDoc = case['case_name']
        res=send_request('post',case['url'],case['data'])
        self.assertEqual(json.loads(case['expect'])['code'],jsonpath(res.json(),'$.code')[0])
