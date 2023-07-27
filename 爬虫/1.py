#@Authar:Litter_hui
#@time:2022/1/3  10:19
#@name:PyCharm
#---------coding:utf-8--------
import requests
import re
import json
import pprint
import time
import xlwt


def geturl():
    head={'Accept':'application/json, text/plain, */*',
          'Cookie':'EDUWEBDEVICE=c4e3b00cb2fc4f23afa78ccdc368ab62; __yadk_uid=3yRWXg6sAuLV2u0gKYqzqe1AOuw8Fe5Q; WM_TID=dL9tPHJaYFZBBBQBFEcvosdhH1lY9NPE; MOOC_PRIVACY_INFO_APPROVED=true; hasVolume=true; videoVolume=0.8; hb_MA-A976-948FFA05E931_source=www.baidu.com; videoResolutionType=3; videoRate=1.5; __utmz=63145271.1640931165.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=63145271.1807245085.1640931165.1640931165.1640948341.2; NTESSTUDYSI=53cad81212484b37a0005b9af99047f8; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1640845060,1640931162,1641095140,1641168217; WM_NI=SIpSue9eBVK7ZYKvJ%2F87d%2FkrOSNMSWOZUja4LSMQg%2F5Td0b1MF64%2FeHe408TG4WpRCUBa44wHCYKk7pp1fuC6X%2BcIuXwwPgcZdod0OVbsSPq4f8cNBFduJBoVXzOofglcDI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8bf26a88e88599e65fae9a8aa3d54f868f8faef83d9294a3a4f1219ab98fd2f82af0fea7c3b92a9197c0b4f86ffbbb8eb7ca3d9a878597c925fce9acd0ea7a8d8d82aed25d8d869b8be440908d83b2e625f78cacd1e13b8f9afad5ae6f8cbbfcd1bb6085ec9991d149979eafd5b77d8c9d97acea3db4b0ff87f849f688e584cc7f9ca9b9b1e6699abca185b34596bebdb4d37bf8baf884cd4a86bcbbabc1659688b6b0ee6ea5b4ada5cc37e2a3; STUDY_INFO="UID_1504FEB1657C3D48DEF6B645D5DFE589|4|1396871027|1641168230186"; NETEASE_WDA_UID=1396871027#|#1564054112690; CLIENT_IP=220.196.192.205; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1641179200',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
    url= 'https://www.icourse163.org/learn/SWJTU-1002529022?tid=1463211442#/learn/testlist'
    print(url)
    try:
        response = requests.get(url=url,headers=head)
        #if response.content:
        js = json.loads(response.text)
    except json.JSONDecodeError:
        print(url)
        print(js)

    pprint.pprint(js)


if __name__ == '__main__':
    geturl()
