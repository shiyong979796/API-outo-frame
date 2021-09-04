import unittest
import requests
from api.cart import CART_API
from api.login import LoginAPI
import config
import time

data = {
    "email": "ys@tetx.com",
    "password": "123456"
}
rec_id=None



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
        login_response=self.new_api.login(self.session,data)#调用登录 传session
        cart_list_repones=self.new_cart.cart_list(self.session)
        self.assertEqual(0,cart_list_repones.json().get('code'))
        self.assertEqual(True,cart_list_repones.json().get('data').get('available'))



    def test02_add_cart(self):
        print('添加商品到购物车')
        commodity_attribute={
            'goods_id': "1006623",
            'goods_number': '1',
            "dress_type": "dress",
            'styles[select][size]': 6765,
            'styles[select][color]': 11630,
            "email": "ys@tetx.com",
            "password": "123456"
        }
        add_cart_response=self.new_cart.cart_api(self.session,commodity_attribute)
        print('respones：',add_cart_response.json())
        self.assertEqual(0,add_cart_response.json().get('code'))
        self.assertEqual('success', add_cart_response.json().get('msg'))
        rec_id=add_cart_response.json().get('data').get('rec_id')
        return  rec_id




    def test03_updata_cart(self):
        print('修改购物车内商品数量')
        data2 = {
            'goods_number': 5
        }
        url='https://apix.azazie.com/1.0/cart/goods/{}'.format(Test_cart.test02_add_cart(self))
        print(url)
        updata_cart_response =self.new_cart.updata_cart(self.session,url,data2)
        print('respones：',updata_cart_response.json())
        self.assertEqual(0,updata_cart_response.json().get('code'))
        self.assertEqual('success', updata_cart_response.json().get('msg'))
