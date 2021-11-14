import requests
import path
import json
from path import get_headers

headers=get_headers()

url_login='https://apix.azazie.com/1.0/user/login'
url_showroom="https://apix.azazie.com/1.0/showroom"
add_cart_url = r"{}/1.0/cart/goods".format(path.PROD_URL)
cart_list_url = r"{}/cart".format(path.PROD_URL)
session=requests.session()


account={
    "email":"ys@tetx.com",
    "password":"123456"
}


commodity_attribute = {
    "act": "addGoodsToCart",
    'goods_id':1002167,
    'goods_number':1,
    "dress_type":"dress",
    "select": {"color": 11629,
               "size": 6765
            }
}

data = {"act": "addGoodsToCart",
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


# #加车
# url='https://api-t-7.azazie.com/1.0/cart/goods'
# token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYzNTE0OTgyMiwiZXhwIjoxNjM1NzU0NjIyLCJ1c2VyX2lkIjoyODI0MTc3fQ.UmQtXHDcGfu1SWjbr19HmsjOQ1mQLSsVhGlyuitHa-s'
# response=requests.post(url=url,json=data,headers=get_headers(token))
# print(response.json())

#登录
# response=requests.post(url_login,json=account,headers=headers)
# print(response.json())

# from jsonpath import jsonpath
# login_url = "http://api.lemonban.com/futureloan/member/login"
# login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
# # resp = send_requests("POST", login_url, login_datas)
# bb=response=requests.post(login_url,json=login_datas)
# print(bb.json())
# code=jsonpath(bb.json(),'$.code')[0]
# code2=bb.json()['code']
# print(type(code),type(code2))

a={

    "code": 0,
    "error": "",
    "msg": "success",
    "data": {"user_id": 4738962,
        "email": "pvpvpv@tetx.com",
        "name": "pvpvpv",
        "cartNumChanged": False,
        "isPreviewUser": False
    }
}

print(a)