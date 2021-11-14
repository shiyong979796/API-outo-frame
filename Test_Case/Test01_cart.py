import unittest
import requests
from api.cart import CART_API
from api.login import LoginAPI
from common.handle_cf_file import new_cfFile as cf
from common.handle_request import get_headers
from common.handle_log import new_log
from common.handle_data import Global_var
from common.handle_request import send_request
from jsonpath import jsonpath
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
        email,password=cf.get_str('Account','old_email'),cf.get_str('Account','password')
        response=new_login.login({"email":email,"password":password})
        cls.token=jsonpath(response.json(),'$.data.token')[0]

    def setUp(self):
        self.new_cart=CART_API()





    def test02_add_cart(self):
        print('添加商品到购物车')
        commodity_attribute={
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
        res=self.new_cart.cart_api(commodity_attribute,get_headers(self.token))
        rec_id=str(res.json()['data']['rec_id'])
        setattr(Global_var,'rec_id',rec_id)
        self.assertEqual(0,res.json().get('code'))
        self.assertEqual('success', res.json().get('msg'))


    def test03_remove_cart(self):
        new_log.info("*********   执行用例{}  *********".format('删除购物车'))
        self._testMethodDoc = '删除购物车商品'
        rec_id=getattr(Global_var,'rec_id')
        data={"is_real_delete":"false"}
        res=send_request('delete','/cart/goods/{}'.format(rec_id),data,self.token)
        expect={'code': 0, 'error': '', 'msg': 'success', 'data': {}}
        self.assertEqual(res.json(),expect)




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
