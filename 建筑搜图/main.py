# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 22:04
# @Author  : Garnetsky
# @FileName: main.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import requests
def main():
    data = requests.get("https://api.map.baidu.com/panorama/v2",  params={"ak": "zX6agbeWsZKFs6VMtrzDtgcFZFoRwj0g","location":"121.508076,31.237675","heading":120})
    with open('./1.jpeg','wb') as f:
        f.write(data.content)

main()