# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 18:03
# @Author  : Garnetsky
# @FileName: selenium_test.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top


from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()
web.get("https://msg.zzuli.edu.cn/xsc/view")
web.find_element('div').send_keys()

# 跳转窗口
web.switch_to.window(web.window_handles[-1])

# 关闭当前窗口
web.close()

# 处理iframe  先拿到iframe 再切换视角到iframe
frame = web.find_element_by_css_selector('iframe')
web.switch_to.frame(frame)

# 切换回原页面
web.switch_to.default_content()