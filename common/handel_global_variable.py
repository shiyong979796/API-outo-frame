#:@ TIME 2021/10/30   22:32
#:@FILE  handel_global_variable.py
#:@EMAIL  1557225637@QQ.COM
import jsonpath
import re
import json
from common.handle_cf_file import new_cfFile as cf
from common.handle_ddt import new_register_data,Global_var
data="{case_name': '充值成功', 'data': '{\"email\":\"#email#\",\"password\":\"#password#\",\"user\":\"#user#\"}', 'expect': '{\"code\": 0, \"msg\": \"success\", \"money\": 3696.99}', 'check_sq': 'SELECT CAST(users.MONEY as CHAR)  as MONEY FROM `users` WHERE  PHONE=16628554195 AND `PASSWORD`=123456'}"


'''
替换字符串中的关键字

引入 re 正泽表达式
用正泽表达式 查询返回出 关键字 in list
for 循环列表内的关键字，通过 调用配置文件 or 全局变量  获取值
然后 传入的字符串 case 进行关键字替换  返回值重新赋值给case

'''

def replace_all_data(case):
    case=json.dumps(case) #转化字符串

    res=re.findall("#(.*?)#",case)#正泽提取关键字key  list

    #循环 list  获取值 替换到 case
    if res:
        for item in res:
            try:
                value=str(cf.get_str('Account',item))
            except:
                try:
                    value=str(getattr(Global_var,'user'))
                except:
                    # continue
                    value="#{}#".format(item)
            case=case.replace("#{}#".format(item),value)  #替换后赋值给kys
            case=json.loads(case)
        return case

