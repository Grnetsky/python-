# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 20:14
# @Author  : Garnetsky
# @FileName: sign in.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import time
import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome import options
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from selenium.webdriver.common.by import By
import sendEmail

from apscheduler.schedulers.blocking import BlockingScheduler

sch = BlockingScheduler(timezone="Asia/Shanghai")


def main():
    print("123")
    try:
        op = options.Options()
        op.add_argument('--headless')
        op.add_argument('--disable-gpu')
        web = Chrome(options=op)
        web.get('https://msg.zzuli.edu.cn/xsc/week?spm=0&code=f142c0f91fbc37f79d1ccfa18a071eba&from=h5')
        day = datetime.datetime.now().day
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date_time = "%4d-%02d-%02d" % (year, month, day)
        print(date_time)
        item = web.find_element(By.CSS_SELECTOR, 'span[data-day="' + date_time + '"')
        item.click()
        web.find_element(By.CSS_SELECTOR, '.wj-btn>a').click()
        time.sleep(2)
        web.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入联系电话"]').send_keys('15523954133')
        web.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入家庭（家长）联系电话"]').send_keys('13761828962')
        web.find_element(By.CSS_SELECTOR,
                         '#app > div > div:nth-child(3) > div:nth-child(30) > div.van-cell-group.van-hairline--top-bottom > div > div > div > textarea').send_keys(
            '无')
        web.execute_script('''
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(2) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(8) > div.van-cell-group.van-hairline--top-bottom > div > div > div > div > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(10) > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(18) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(23) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(3) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(25) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(27) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(28) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click();
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(29) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click()
        document.querySelector('#app > div > div:nth-child(3) > div:nth-child(29) > div > div.van-cell-group.van-hairline--top-bottom > div > div:nth-child(1) > div > i').click()
        ''')
        location_text = ''
        while not len(location_text) > 2:
            web.find_element(By.CSS_SELECTOR,
                             '#app > div > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div.van-cell-group.van-hairline--top-bottom').click()
            time.sleep(5)
            print(location_text)
            location_text = web.execute_script(
                "return document.querySelector('#app > div > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div.van-cell-group.van-hairline--top-bottom > div > div > div > textarea').value")
        web.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(3) > div.submit-div > button').click()
        time.sleep(2)
        info = web.find_element(By.CSS_SELECTOR, 'body > div.van-dialog > div.van-dialog__content > div').text
        print(info)
        defalut_info = "12、您今日的体温：正常 13、您今日有无以下症状：无 14、今日同住人员身体状况：无 15、您假期以来是否接触过疑似或确诊病例：否 16、是否被当地要求到指定地点隔离：否 18、完成疫苗接种情况：已完成接种 19、10月以来本轮郑州疫情核酸检测次数：未检测 20、所在地风险等级：低风险 21、所在区域管理分类：正常 22、国家政务服务平台健康码状态：绿色 23、其他需要说明的情况：无 是否确认提交"
        location = re.search('目前您的位置和居住地点：\S+', info).group()

        # 判断是否为本地 否则会报错
        isSH = re.search('上海市金山区', location).group()
        print(location, isSH)

        # 判断其他数据是否相同 是则通过 否则抛出异常
        outinfo = re.search('12.+', info).group()
        if outinfo in defalut_info:
            print("数据正常")
            time.sleep(5)
            web.find_element(By.CSS_SELECTOR,
                             'body > div.van-dialog > div.van-hairline--top.van-dialog__footer.van-dialog__footer--buttons > button.van-button.van-button--default.van-button--large.van-dialog__confirm.van-hairline--left').click()
            time.sleep(5)
            web.close()
        else:
            print("数据异常")
            raise Exception("数据异常")

        result = sendEmail.send_email('打卡成功', info)

        if result:
            with open('jiankang_log.txt', 'a') as f:
                f.write(date_time + '成功打卡' + location + '\n')

    except Exception as e:
        print(e)
        result = sendEmail.send_email("今日打卡失败", "今日打卡失败 详情为" + str(e))
        web.close()
        print("出错了")

    # 执行js代码


if __name__ == '__main__':
    sch.add_job(main, 'cron', hour=0, minute=6, end_date='2022-12-19')
    sch.start()
