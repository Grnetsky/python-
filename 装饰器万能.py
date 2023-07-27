import time


def set_fun(func):  # func = a(*args,**kwargs)

    print("----hhh---")

    def call_fun(*args,**kwargs):
        strat_tame = time.time()
        print("开始装饰")
        stop_time = time.time()
        all_time = stop_time - strat_tame
        print(all_time)
        return func(*args,**kwargs)
    return call_fun


@set_fun
def a(*args,**kwargs):
    print("---原函数---")
    print("元组：",args)
    print("字典",kwargs)
    return "xxxx"


b = a(1, 2, mm=100)
print(b)

