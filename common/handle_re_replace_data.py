#:@ TIME 2021/10/30   22:32
#:@FILE  handle_re_replace_data.py
#:@EMAIL  1557225637@QQ.COM
import jsonpath
import re
import json
from common.handle_cf_file import new_cfFile as cf
from common.handle_data import Global_var
data="{case_name': '充值成功', 'data': '{\"email\":\"#email#\",\"password\":\"#password#\",\"user\":\"#user#\"}', 'expect': '{\"code\": 0, \"msg\": \"success\", \"money\": 3696.99}', 'check_sq': 'SELECT CAST(users.MONEY as CHAR)  as MONEY FROM `users` WHERE  PHONE=16628554195 AND `PASSWORD`=123456'}"






# if __name__ == '__main__':
#     import random
#     cc=''.join(random.sample('abcdefghijklmnopqrstuvwxyz',8))
#     print(cc)
#     setattr(Global_var,'email',cc)
#
#
#     aa={'id': 1, 'case_name': '注册成功', 'data': '{"email":"#email#@tetx.com","password":"123456"}',
#      'expect': "{'code': 0, 'msg': 'success', 'data': {'user_id': True, 'email': '#email#@tetx.com.com', 'name': 'ys', 'cartNumChanged': False}}",
#      'msg': 'success', 'check_sql': 'select  * form  …'}
#     aa=replace_all_data(aa)
#     print(aa)