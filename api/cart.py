import requests
from config import HEADER
import config  #导入配置模块

class CART_API:
    def __init__(self):
        self.add_cart_url='{}/1.0/cart/goods'.format(config.PROD_URL)
        self.cart_list_url=r"{}/cart".format(config.PROD_URL)

    '''
    Body Parameters
    Parameter	        Type	Status	Description
    goods_id	        integer	optional	商品id
    custom	            string	optional	是否自定义尺码
    goods_number	    integer	optional	商品数量
    dress_type	        string	optional	商品dress_type
    styles	            array	optional	商品style数据
    styles_sash	        array	optional	腰带
    from_showroom	    string	optional	是否来源showroom
    from_instagram	    string	optional	是否来源instagram
    from_detail_entry	string	optional	商品加车来源
    from_whatAreU	    string	optional	商品加车来源
    '''
    def cart_api(self,session,commodity_attribute):
        return  session.post(url=self.add_cart_url,data=commodity_attribute)

    def updata_cart(self,session,url,data):
        return session.post(url=url,data=data)

    def cart_list(self,session):
        return session.get(self.cart_list_url)