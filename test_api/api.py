import requests
import config
import json
from config import get_headers

#
# url_login='https://apix.azazie.com/1.0/user/login'
# url_showroom="https://apix.azazie.com/1.0/showroom"
add_cart_url = r"{}/1.0/cart/goods".format(config.PROD_URL)
# cart_list_url = r"{}/cart".format(config.PROD_URL)
# session=requests.session()
#
#

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



url='https://api-t-7.azazie.com/1.0/cart/goods'
token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYzNTE0OTgyMiwiZXhwIjoxNjM1NzU0NjIyLCJ1c2VyX2lkIjoyODI0MTc3fQ.UmQtXHDcGfu1SWjbr19HmsjOQ1mQLSsVhGlyuitHa-s'
response=requests.post(url=url,json=data,headers=get_headers(token))
print(response.json())

