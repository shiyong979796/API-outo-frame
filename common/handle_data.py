#:@ TIME 2021/11/5   15:49
#:@FILE  handle_data.py
#:@EMAIL  1557225637@QQ.COM
from jsonpath import jsonpath
import re
from common.handle_cf_file import new_cfFile as cf
from common.handle_log import new_log


class  Global_var:
    """
       存储用例要使用到的数据。
       """
    pass



def Clear_global_var():
    """
       清除用例要使用到的数据。
       """
    value=dict(Global_var.__dict__.items())
    for  key,value in value.items():
        if key.startswith("__"):
            pass
        else:
            delattr(Global_var,key)



def extract(extract_data,response):

    '''
    根据jsonpath提取表达式，从响应结果当中，提取数据并设置为环境变量EnvData类的类属性，作为全局变量使用。
    :param extract_data: 从excel当中读取出来的，提取表达式的字符串。
    :param response: http请求之后的响应结果。
    :return:Nonoe
    """
    '''
    dict_extract_data=eval(extract_data)
    for key,value in dict_extract_data.items():
        res=jsonpath(response,value)[0]
        setattr(Global_var,key,res)


def replace_all_data(case):
    for key,value in case.items():
        if value is not None and isinstance(value,str):
            case[key]=__replace_data(value)
    new_log.info("正则表达式替换完成之后的请求数据：\n{}".format(case))
    return case



def __replace_data(data):
    '''
    替换字符串中的关键字

    引入 re 正泽表达式
    用正泽表达式 查询返回出 关键字 in list
    for 循环列表内的关键字，通过 调用配置文件 or 全局变量  获取值
    然后 传入的字符串 case 进行关键字替换  返回值重新赋值给case

    '''
    # 正泽提取关键字key  list
    res=re.findall("#(.*?)#",data)

    #循环 list  获取值 替换到 case
    if res:
        for item in res:
            try:
                value=str(cf.get_str('Account',item))
            except:
                try:
                    value=str(getattr(Global_var,item))
                except:
                    continue
                    # value="#{}#".format(item)
            # 替换后赋值给kys
            data=data.replace("#{}#".format(item),value)
    return data
#
# def replace_data(data):
#     """
#     将字符串当中，匹配#(.*?)#部分，替换换对应的真实数据。
#     真实数据只从2个地方去获取：1个是配置文件当中的data区域 。另1个是，EvnData的类属性。
#     data: 字符串
#     return: 返回的是替换之后的字符串
#
#     ps： 1个是配置文件当中的data区域 。另1个是，EvnData的类属性。必须都是字符串类型。
#     """
#     res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表。
#     # 标识符对应的值，来自于：1、环境变量  2、配置文件
#     if res:
#         for item in res:
#             # 得到标识符对应的值。
#             try:
#                 value = conf.get("data", item)
#             except:
#                 try:
#                     value = getattr(EnvData, item)
#                 except AttributeError:
#                     # value = "#{}#".format(item)
#                     continue
#             print(value)
#             # 再去替换原字符串
#             data = data.replace("#{}#".format(item), value)
#     return data



def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case
