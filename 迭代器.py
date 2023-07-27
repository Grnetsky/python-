import time
class Classmater(object):
    def __init__(self):
        self.name = list()
        self.num = 0
    def add(self,name):
        self.name.append(name)

    def __iter__(self):
        return self #返回一个迭代器的next方法

    def __next__(self):

        if self.num < len(self.name):

            ret = self.name[self.num]
            self.num += 1
        else:
            raise StopIteration

        return ret

a = Classmater()

a.add("li")
a.add("hao")
a.add("str")

for i in a:
    print(i)
    time.sleep(0.5)

