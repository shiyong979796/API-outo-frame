#:@ TIME 2021/10/9   21:16
#:@FILE  test.py
#:@EMAIL  1557225637@QQ.COM
from utlis import Database
import random

'''
获取手机号


def get_phone():
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


dict={'a':'2',"b":"1","c":"5","d":"1","e":"4","f":1}

def find_data(case,newd,oldd):
    for key,value in case.items():
        if  value is not None and isinstance(value,str):
            if value.find(oldd) !=-1:
                case[key]=newd
    return case


dict=find_data(dict,'new','1')
print(dict)