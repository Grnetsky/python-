


class A(object):
    def __init__(self):
        self.value = 0
#新式类 有property setter deleter三个内置属性
    @property
    def setvalue(self):
        return self.value

    @setvalue.setter
    def setvalue(self,value):
        if value == "hhh":
            raise ValueError("不能为hhh")

        else:
            self.value = value

    @setvalue.deleter
    def setvalue(self):
        self.value = 0

a = A()

a.setvalue = 12
# a.setvalue = "hhh"
del a.setvalue
print(a.value)


