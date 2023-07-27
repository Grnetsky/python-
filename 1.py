# import requests
#
# def get_reason(question):
#     url = "https://www.hive-net.cn:8443/wechat/search/?token=free&question=" + question
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         print(r.json()['reason'])
#     except:
#         print("Fail")
#
# get_reason("在什么情况下N95口罩需要更换?")

def foo():
    print(a)

def bar ():
    a = 3
    def foo():
        print(a)
    foo()

a = 2
bar()


def x(m):
    print("666",m())
    m()


def c():
    print("ccc")
    return "cxcxcx"
