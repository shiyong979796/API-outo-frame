#:@ TIME 2021/10/31   23:16
#:@FILE  atest_yewuliu.py
#:@EMAIL  1557225637@QQ.COM
import unittest
from ddt import ddt,data
from common.handle_data import Global_var,Clear_global_var
from common.handle_excel import Excel_data
from common.handle_data import extract,replace_all_data
from common.handle_log import new_log
from common.handle_new_email import get_new_emai
from common.handle_request import send_request

import path
new_register_data=Excel_data(path.excel_dir + '\\excel_data.xlsx', 'ywls')#创建ddt对象print(data1)
case=new_register_data.all_data()

@ddt()
class Test_ywl(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        new_log.info("======  加车用例 开始执行  ========")
        email=get_new_emai()
        setattr(Global_var,'email',email)


    @classmethod
    def tearDownClass(cls) -> None:
        new_log.info("======  加车用例 执行结束  ========")
        Clear_global_var()


#注册
    @data(*case)
    def test_ywl(self,case):
        new_log.info("测试点:{}".format(case['case_name']))
        case=replace_all_data(case)
        if hasattr(Global_var,'token'):
            res=send_request(case['method'],case['url'],case['data'],token=getattr(Global_var,'token'))
        else:
            res = send_request(case['method'], case['url'], case['data'])
        #如果 用例需要提取参数  就调用提取方法  提取响应数据 设置为全局变量
        if case['extract_data']:
            extract(case['extract_data'],res.json())


#登录   账号  密码
#加车 token
#删车



















































