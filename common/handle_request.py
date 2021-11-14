#:@ TIME 2021/11/1   14:27
#:@FILE  handle_request.py
#:@EMAIL  1557225637@QQ.COM
import requests
import json
from common.handle_log import new_log
from common.handle_cf_file import new_cfFile as conf
def send_request(method,url,data,token=None):
    new_log.info("发起一次HTTP请求")

    #拼接url
    url=__join_url(url)
    # 得到请求头
    headers=get_headers(token)
    #请求头转大写
    method=method.upper()

    #如果data 是 str 就转成字典
    data=__pre_data(data)


    #调用请求 输出log
    new_log.info("请求头为：{}".format(headers))
    new_log.info("请求方法为：{}".format(method))
    new_log.info("请求url为：{}".format(url))
    new_log.info("请求数据为：{}".format(data))

    if method == 'GET':
        if url=='http://127.0.0.1:8899/money':
            return None
        res=requests.get(url,headers=headers)
        new_log.info("响应状态码为：{}".format(res.status_code))
        new_log.info("响应数据为：{}".format(res.json()))
        return res

    elif method == 'POST':
        res=requests.post(url,json=data,headers=headers)
        new_log.info("响应状态码为：{}".format(res.status_code))
        new_log.info("响应数据为：{}".format(res.json()))
        return res

    elif method == 'DELETE':
        res= requests.delete(url,json=data,headers=headers)
        new_log.info("响应状态码为：{}".format(res.status_code))
        new_log.info("响应数据为：{}".format(res.json()))
        return res
    elif method == 'PUT':
        res=requests.put(url,json=data,headers=headers)
        new_log.info("响应状态码为：{}".format(res.status_code))
        new_log.info("响应数据为：{}".format(res.json()))
        return res



def __join_url(url):
    """
    拼接接口的url地址。
    """
    base_url = conf.get_str("Url", "PROD_URL")
    if url.startswith("/"):
        return base_url + url
    elif url.endswith('money'):
        return r'http://127.0.0.1:8899/money'
    else:
        return base_url + "/" + url


def __pre_data(data):
    """
    如果data是字符串，则转换成字典对象。
    """

    if data is not None and isinstance(data,str):
        if data.find('null') !=-1:
            data=data.replace('null','None')
        return eval(data)
    #     try:
    #         return json.loads(data)
    #     except:
    #         return eval(data)
    # return data

def get_headers(token=None):
    header={"Content-Type":"application/json",
            "Accept":"application/json",
            "x-app":"pc",
            "x-token":"",
            "x-project":"azazie",
            "x-countryCode":"US"
            }
    if token:
        header["x-token"]=token
    return header

# if __name__ == '__main__':
#     url = __join_url(r'http://127.0.0.1:8899/money')
#     print(url)
#     # data={
#     #     "email":"ys@tetx.com",
#     #     "password":"123456"
#     # }
#     # send_request('post',url,data)
#     requests.post(url=url,json=)
