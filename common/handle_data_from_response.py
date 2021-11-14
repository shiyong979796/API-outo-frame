#:@ TIME 2021/11/4   1:43
#:@FILE  handle_data_from_response.py
#:@EMAIL  1557225637@QQ.COM
from jsonpath import jsonpath
from common.handle_data import Global_var
# class Var:
#     pass



# if __name__ == '__main__':
#
#     commodity_attribute = {
#         "act": "addGoodsToCart",
#         "goods_id": 1002167,
#         "dress_type": 'dress',
#         "from_showroom": "",
#         "from_whatAreU": "",
#         "recommend_flag": "",
#         "from_details_entry": "",
#         "from_instagram": "",
#         "styles": {
#             "freeStyle": False, "size_type": "_inch",
#             "select": {
#                 "color": 11629, "size": 6765
#             }
#         },
#         "goods_number": 1
#     }
#     b="{'act': 'addGoodsToCart', 'goods_id': 1002167, 'dress_type': 'dress', 'from_showroom': '', 'from_whatAreU': '', 'recommend_flag': '', 'from_details_entry': '', 'from_instagram': '', 'styles': {'freeStyle': False, 'size_type': '_inch', 'select': {'color': 11629, 'size': 6765}}, 'goods_number': 1}"
#     print(commodity_attribute)
#     b=eval(b)
#     for key,value in b.items():
#         print(key,value)