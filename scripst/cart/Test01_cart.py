import unittest
import requests
from api.cart import CART_API
from api.login import LoginAPI
import config
import time

class Test_cart(unittest.TestCase):


    # 后置方法
    def tearDown(self):
        # 关闭session对象
        if self.session:
            self.session.close()

    #前置方法
    def setUp(self):
        self.new_cart=CART_API()
        self.new_api=LoginAPI()
        self.session=requests.session()

    # def add_cart(self):


    #获取购物车列表
    def test01_cart_list(self):
        print('获取购物车列表')
        data = {
            "email": "ys@tetx.com",
            "password": "123456"
        }

        login_response=self.new_api.login(self.session,data)#调用登录 传session
        cart_list_repones=self.new_cart.cart_list(self.session)
        self.assertEqual(0,cart_list_repones.json().get('code'))
        self.assertEqual(True,cart_list_repones.json().get('data').get('available'))

