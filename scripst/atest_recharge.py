#:@ TIME 2021/10/28   1:17
#:@FILE  atest_recharge.py
#:@EMAIL  1557225637@QQ.COM
from unittest import TestCase
from api.recharge import Recharge
from api.login import LoginAPI
from common.handle_cf_file import new_cfFile as cf
from common.handle_ddt import Ddt_data
from common.handel_log import new_log
from common.handle_database import Database
from common.handel_replace_data import replace_data
from ddt import ddt,data
import json
import os
import config
import unittest

new_ddt = Ddt_data(os.path.join(config.data_dir,'recharges.xlsx'),'recharge')

@ddt()
class Test_payment(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.new_recharge=Recharge()
        mew_login=LoginAPI()
        cls.email,cls.password=cf.get_str('Account','email'),cf.get_str('Account','password')
        cls.db=Database()

    @data(*new_ddt.all_data())
    def test_recharges(self,case):
        self._testMethodDoc=case['case_name']
        if case['check_sq']:
            db_money=float(self.db.get_fetchone(case['check_sq'])['MONEY'])  #查询数据库当前余额
            new_log.debug('当前数据库余额：{}'.format(db_money))
            add_money=float(json.loads(case['data'])['money']) #获取用例增加的额度

            sum_money=db_money+add_money
            case=replace_data(case,str(sum_money),'#new_money#')
            new_log.debug('替换后的case：{}'.format(case))

        response=self.new_recharge.recharge(json.loads(case['data']))
        new_log.debug('接口响应参数:{}'.format(response.json()))

        self.assertEqual(json.loads(case['expect'])['code'],response.json()['code'])
        if case['check_sq']:
            self.assertEqual(sum_money,float(response.json()['money']))



