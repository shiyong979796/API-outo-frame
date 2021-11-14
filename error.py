# # try:
# #     a=int(input("请输入一个整数"))
# #     b=int(input('请输入一个整数'))
# #     print(a/b)
# # except ValueError:
# #     print("输入的非整数")
# #
# # except ZeroDivisionError:
# #     print('输入的数不能为0')
# #
# # except :
# #     print('未知错误')
#
#
# # import unittest
# # from parameterized import parameterized
# # parmeters=[(1,2,7),(5,2,7),(4,4,9)]
# # class my_test(unittest.TestCase):
# #
# #
# #     @parameterized.expand(parmeters)
# #     def test11111(self,a, b,c):
# #         # print('test 111111')
# #         d=a+b
# #         self.assertEqual(c,d)
# #         print(a,b,c)
# #
# #     @unittest.skip
# #     def testa(self):
# #         print('跳过此方法')
# #
#
# # import unittest
# # from parameterized import parameterized
# # class shi(unittest.TestCase):
# #     @parameterized.expand([(1,2,3,4),(5,6,7,8),("a","b","c","d")])
# #     def test_111(self,a,b,c,d):
# #         print(a,b,c,d)
# #         print(1111)
# #
# #
# # suite1=unittest.TestSuite()
# # suite1.addTest(shi("test_01"))
# #
# # test_runner=unittest.TextTestRunner()
# # test_runner.run(suite1)
# #
# #
# # import requests
# # import config
# # from api.cart import CART_API
# # from api.login import LoginAPI
# # # def post_api(url,body,header):
# # #     return requests.get(url=url,json=body,heards=header)
# # #
# # # def get_api(url,header):
# # #     return requests.post(url=url,heards=header)
# # url='https://apix.azazie.com/1.0/cart'
# #
# HEADER={
# "Content-Type":"application/json",
# "Accept":"application/json",
# "x-app":"pc",#pc|android|ios|h5
# "x-project":"azazie",
# "x-countryCode":"us"#US|CA 国家短码
# }
# data = {
#     "email": "ys@tetx.com",
#     "password": "123456"
# }
# # url_login='https://apix.azazie.com/1.0/user/login'
# #
# # newlogin=LoginAPI()
# # newcart=CART_API()
# # session1=requests.session()
# # # responese=session1.post(url=url_login,json=data,headers=HEADER)
# # re=newlogin.login(session1,data)
# # print(re.json())
# # cr=newcart.cart_list(session1)
# # print(cr.json())
# # # print(responese.json())
# from api.cart import CART_API
# from api.login import LoginAPI
# import requests
# new_cart = CART_API()
# new_api = LoginAPI()
# session = requests.session()
#
# print('添加商品到购物车')
#
#
#
# commodity_attribute = {
#     'goods_id':"1006623",
#     'goods_number':'1',
#     "dress_type":"dress",
#     'styles[select][size]':6765,
#     'styles[select][color]':11630,
#     "email":"ys@tetx.com",
#     "password":"123456",
#     'X-Token':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYzMDA4MDQ3NiwiZXhwIjoxNjMwNjg1Mjc2LCJ1c2VyX2lkIjozODU2MDU4fQ.fbjocjjDD1EeULs5gpQ9Lvgye4TBS-J9B7-SDjF3PTI"
# }
# url_login='https://apix.azazie.com/1.0/user/login'
# responese=session.post(url=url_login,json=data,headers=HEADER)
# print(responese.json())
# url1='https://apix.azazie.com/1.0/cart/goods'
#
# response=session.post(url=url1,data=commodity_attribute)
# recid=response.json().get('data').get('rec_id')
# # response =new_cart.cart_api(session,commodity_attribute)
# print('respones：', response.json())
#
#
#
# url2='https://apix.azazie.com/1.0/cart/goods/{}'.format(recid)
# data2={
#     'goods_number':"10"
# }
# response2=session.post(url=url2,data=data2)
# print(response2.json())
# from utlis import Database
# from utlis import Config_file
# cf=Config_file()
#
#
# if __name__ == '__main__':
#     ccc = cf.get_str('Host', 'host')
#     print(ccc)
# case={"case_name":"测试用例名称",'data':{"email":"test_name","passowrd":"123456"}}
# print(case['data']['email'])
# a='ss@tetx.com'
# print(a)
# c=a[-9:]
# print(c)#反向切片print(names[-1::-1])#反向切片
# import os
# import utlis
# import path
# cf=utlis.Config_file(os.path.join(path.conifg_file_dir, 'config_file.ini'))
# print(cf.get_str('Hosta','host'),cf.get_int('attribute','port'),cf.get_str('attribute','user'),
#                   cf.get_str('attribute','password'),cf.get_str('attribute','database'))
# db=utlis.Database()

# result=db.get_fetchall('SELECT * FROM users WHERE email ="outotest@tetx.com2803598"')
# print(result)‘

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
# print(commodity_attribute)
# {"token":"$.data.token)[0]","rec_id":"$.data.rec_id)[0]"}
#
# from jsonpath import jsonpath
# a={'code': 0, 'error': '', 'msg': 'success', 'data': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYzNTk2MDY5MywiZXhwIjoxNjM2NTY1NDkzLCJ1c2VyX2lkIjoyODI0MTc3fQ.HZOW0Oplhy7BXUTTwz08ph11-9VfGXyq6EvVjGBJ_70', 'user_id': 2824177, 'email': 'ys@tetx.com', 'name': 'ys', 'cartNumChanged': False, 'isPreviewUser': False}}
#
# print(jsonpath(a,'$.data.token')[0])
# a= "{'act': 'addGoodsToCart', 'goods_id': 1002167, 'dress_type': 'dress', 'from_showroom': '', 'from_whatAreU': '', 'recommend_flag': '', 'from_details_entry': '', 'from_instagram': '', 'styles': {'freeStyle': False, 'size_type': '_inch', 'select': {'color': 11629, 'size': 6765}}, 'goods_number': 1}"
# a=eval(a)
# print(a)
# for  key,value  in a:
#     print(key,value)
# from jsonpath import jsonpath
# import json
# bb="{'act': 'addGoodsToCart', 'goods_id': 1002167, 'dress_type': 'dress', 'from_showroom': '', 'from_whatAreU': '', 'recommend_flag': '', 'from_details_entry': '', 'from_instagram': '', 'styles': {'freeStyle': False, 'size_type': '_inch', 'select': {'color': 11629, 'size': 6765}}, 'goods_number': 1}"
# if bb.find('False') or bb.find('True'):
#     bb=bb.replace('False','"false"')
#     bb=bb.replace('True','"true"')
# bb=json.loads(bb)
# print(bb)


# case=json.loads(bb)

# print(type(commodity_attribute))
# for key,value in commodity_attribute.items():
#     print(key,value)


# a={'pear':"梨"}
# b=input('输入：')
# for  key,value in a.items():
#     print(key,value)
#     if b in value:
#         print('输入正确')
#     else:
#         print('输入错误')


# a={'pear':"梨"}
# b={"apple":"苹果"}
#
# print(a.update(b))


cc='wfsfnullawdwadanull'
if cc.find('null')!=-1:
    dd=cc.replace('null','kkk')
    print(dd)