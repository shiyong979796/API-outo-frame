#:@ TIME 2021/10/9   21:16
#:@FILE  aaatest.py
#:@EMAIL  1557225637@QQ.COM
from utlis import Database
import random

'''
获取手机号


def creat_phone():
    header_list=[135,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198]
    title=random.randint(0,len(header_list)-1)
    header_phone=str(header_list[title])
    for _ in  range(0,8):
        header_phone+=str(random.randint(0,9))
    return header_phone


# aa=get_phone()
# print(aa)

def get_NewPhone():
    db=Database()
    while True:
        phone=get_phone()
        sq = "select * From users  where  PHONE={}".format(phone)
        if db.count_line(sq)==0:
            return phone

phone=get_NewPhone()
print(phone)

'''


# dict={'a':'2',"b":"1","c":"5","d":"1","e":"4","f":1}
#
# def find_data(case,newd,oldd):
#     for key,value in case.items():
#         if  value is not None and isinstance(value,str):
#             if value.find(oldd) !=-1:
#                 case[key]=newd
#     return case
#
#
# dict=find_data(dict,'new','1')
# print(dict)
#
# import random
#
#
# print(''.join(random.sample('abcdefghijklmnopqrstuvwxyz',8)))


# from api.login import LoginAPI
# from common.handle_cf_file import new_cfFile as cf
# def aaa():
#     new_login=LoginAPI()
#
#     response=new_login.login({"email":cf.get_str('Account','user'),"password":cf.get_str('Account','password')})
#     print(response.json())
#     token=response.json()['data']['token']
#     print(token)


# import time
# filename=time.strftime("%Y%m%d-%H%M%S")+'.html'
# print(filename)


import jsonpath
# ass={
#     "code": 0,
#     "error": "",
#     "msg": "success",
#     "data": {
#         "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhemF6aWUiLCJhdWQiOiJ1c2VycyIsImlhdCI6MTYzNTA2NzQ3OCwiZXhwIjoxNjM1NjcyMjc4LCJ1c2VyX2lkIjozODU2MDU4fQ.8_5chIRbszq1813NAQ7j8uW4ASlPNx2IqEOIRx4ix30",
#         "user_id": 3856058,
#         "email": "ys@tetx.com",
#         "name": "ys",
#         "cartNumChanged": False,
#         "isPreviewUser": False
#     }
# }
#
#
# import jsonpath
# bbb=jsonpath.jsonpath(ass,'$.data.token')
# print(*bbb)
# print(bbb[0])


# ku={"16628554195":"123456","ys@tetx.com":"123456"}
# print(ku['16628554195'])
# def indexa(phone,password,moneys):
#     ku={"16628554195":"123456a","ys@tetx.com":"123456","old_money":100}
#     phone=phone
#     password=password
#     if phone and password and moneys:
#         for key,value in ku.items():
#             print(key,value)
#             if phone == key  and password == value:
#                 print(phone,password)
#                 ku["old_money"]+=moneys
#                 res={"code":0,"msg":"success","money":ku['old_money']}
#                 break
#             else:
#                 res={"code":202,"msg":"The account or password is incorrect"}
#     else:
#         res={"code":201,"msg":"Wrong argument"}
#
# indexa('16628554195','123456a',200)
#
# from common.handle_database import Database
# db=Database()
# sq='UPDATE users set MONEY =1000 WHERE 	PHONE=16628554195'
# sq2='SELECT  CAST(users.MONEY as char) as MONEY FROM users WHERE PHONE="{}" AND PASSWORD ="{}"'.format(str(16628554195),str(123456))
# sq3='SELECT users.MONEY FROM `users` WHERE  PHONE=16628554195 AND `PASSWORD`=123456'
# cc=db.get_fetchone(sq3)
# db.commit()
# print(cc)
#
import re
a='sadfghjklk;jkg`12343fdf@878#$3&*(445q__ABRFGHKL;__'
print(re.findall('.',a)) #匹配除“\n”之外的任何单个字符
print(re.findall('\d',a))#	匹配一个数字字符。等价于[0-9]。
print(re.findall('\D',a))#		匹配一个非数字字符。等价于[^0-9]。
print(re.findall('\w',a))#			匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”
print(re.findall('[abcd]',a))
print(re.findall('[a-z]',a))
print(re.findall('[A-Z]',a))
print(re.findall('[A-Za-z1-9]',a))
print(re.findall('.{3}',a)) #匹配所有字符 每三个
print(re.findall('\d{3}',a)) #匹配 三个在一起的数字
print(re.findall('\d{3,5}',a)) #匹配 三个 至 5个在一起的数字
print(re.findall('\d{2,5}?',a)) #跟上问好 ？ 尽可能匹配2个在一起的数字
print(re.findall('\d{2,}',a)) #跟上问好 ？ 尽可能匹配更长在一起的数字
print(re.findall('\d+',a)) #匹配数字






# a="{'code': 0, 'error': '', 'msg': 'success', 'data': {'rec_id': 8394205}}"
#
# re.findall('.rec_id',a)


