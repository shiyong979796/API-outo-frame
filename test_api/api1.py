import requests
import config


def post_api(url,body,header):
    return requests.get(url=url,json=body,heards=header)

def get_api(url,header):
    return requests.post(url=url,heards=header)