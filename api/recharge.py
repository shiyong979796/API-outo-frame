#:@ TIME 2021/10/28   1:13
#:@FILE  recharge.py
#:@EMAIL  1557225637@QQ.COM
import requests
from common.handle_request import get_headers
class Recharge:

    def __init__(self):
        self.url='http://127.0.0.1:8899/money'


    def  recharge(self,data,headers=None):
        return requests.post(url=self.url,data=data,headers=headers)