def set_v_function(name):
    def set_function(fun):
        def call_function(*args,**kwargs):
            print("加载新功能")
            print("欢迎"+name)
            return fun(*args,**kwargs)
        return call_function
    return set_function

name=input("请输入姓名：")
@set_v_function(name)
def a(*args,**kwargs):
    print("--------",args)
    print("--------",*args)
    print("--------",kwargs)




