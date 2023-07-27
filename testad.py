# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 01:23
# @Author  : Garnetsky
# @FileName: testad.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

web = Chrome()
web.get('http://www.baidu.com')

x = web.find_element(By.CSS_SELECTOR,'#s-top-left > a:nth-child(1)')
name = web.execute_script('''
return document.querySelector('#s-top-left > a:nth-child(1)').text
''')
print(name)