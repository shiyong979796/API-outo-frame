#:@ TIME 2021/10/24   1:57
#:@FILE  handel_replace_data.py
#:@EMAIL  1557225637@QQ.COM
import random
'''
字符替换
传入 case，替换的新data  被替换的data
for循环 字典的 key  value
如果 value 是str类型 且不为空、find 查询字符串关键字 判断value是否是要被替换的字符
查询不= -1就替换
'''
def replace_data(case,new,old):
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            if value.find(old) !=-1:
                case[key]=value.replace(old,new)
    return case
# aa={'case_name': '注册成功', 'data':"{'email': '#data#@tetx.com', 'password': '123456'}", 'code': 0, 'msg': 'success', 'check_sql': 'select  * form'}
#
# aa=replace_data(aa,''.join(random.sample('abcdefghijklmnopqrstuvwxyz',8)),'#data#@tetx.com')
# print(aa)