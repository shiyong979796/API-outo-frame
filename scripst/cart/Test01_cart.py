import unittest
import requests
from api.cart import CART_API
from api.login import LoginAPI
from common.handle_cf_file import new_cfFile as cf
from config import get_headers
from common.handel_log import new_log
import jsonpath
# data = {
#     "email": "ys@tetx.com",
#     "password": "123456"
# }
# rec_id=None


# @unittest.skip
class Test_cart(unittest.TestCase):

    # 后置方法
    def tearDown(self):
        # 关闭session对象
        # if self.session:
        #     self.session.close()
        pass
    #前置方法

    @classmethod
    def setUpClass(cls) -> None:
        new_login=LoginAPI()
        email,password=cf.get_str('Account','email'),cf.get_str('Account','password')
        response=new_login.login({"email":email,"password":password})
        cls.token=jsonpath.jsonpath(response.json(),'$.data.token')

    def setUp(self):
        self.new_cart=CART_API()



    #获取购物车列表
    def test01_cart_list(self):
        cart_list_repones=self.new_cart.cart_list(get_headers(token=self.token))
        new_log.warning('购物车列表响应数据:{}'.format(cart_list_repones.json()))
        try:
            self.assertEqual(0,cart_list_repones.json().get('code'))
            self.assertEqual(True,cart_list_repones.json().get('data').get('available'))
        except Exception:
            new_log.warning('购物车列表校验失败,期望结果：{}，实际结果{}'.format([0,True],[cart_list_repones.json().get('code'),cart_list_repones.json().get('data').get('available')]))
            raise  Exception


    def test02_add_cart(self):
        print('添加商品到购物车')
        commodity_attribute=data = {
        "act": "addGoodsToCart",
        "goods_id": 1002167,
        "dress_type": 'dress',
        "from_showroom": "",
        "from_whatAreU": "",
        "recommend_flag": "",
        "from_details_entry": "",
        "from_instagram": "",
        "styles": {
            "freeStyle": False, "size_type": "_inch",
            "select": {
                "color": 11629, "size": 6765
            }
        },
        "goods_number": 1
        }
        add_cart_response=self.new_cart.cart_api(commodity_attribute,get_headers(self.token))
        self.assertEqual(0,add_cart_response.json().get('code'))
        self.assertEqual('success', add_cart_response.json().get('msg'))


    #
    #
    #
    # def test03_updata_cart(self):
    #     print('修改购物车内商品数量')
    #     data2 = {
    #         'goods_number': 5
    #     }
    #     url='https://apix.azazie.com/1.0/cart/goods/{}'.format(Test_cart.test02_add_cart(self))
    #     updata_cart_response =self.new_cart.updata_cart(self.session,url,data2)
    #     self.assertEqual(0,updata_cart_response.json().get('code'))
    #     self.assertEqual('success', updata_cart_response.json().get('msg'))
