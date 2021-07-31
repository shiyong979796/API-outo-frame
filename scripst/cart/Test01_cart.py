import unittest
import requests
from api.cart import CART_API

class Test_cart(unittest.TestCase):

    #前置方法
    def setUp(self):
        self.new_cart=CART_API()

    #后置方法
    def tearDown(self):
        pass


    #获取购物车列表
    def test01_cart_list(self):
        repones=self.new_cart.cart_list()

        self.assertEqual(0,repones.json().get('code'))
        self.assertEqual(False,repones.json().get('data').get('available'))

