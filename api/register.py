#:@ TIME 2021/10/3   12:50
#:@FILE  register.py
#:@EMAIL  1557225637@QQ.COM
import requests
import config

class Register:
    def __init__(self):
        self.url='{}/1.0/user/register'.format(config.PROD_URL)


    def register(self,data):
        return requests.post(self.url,json=data)



