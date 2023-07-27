# def a(x,y):
#     def s(a):
#         print(a*x+y)
#     return s
# b = a(1,2)
# b(1023)
#
#

import retry
class A():
    def __init__(self):
        self.name = 'a'

    def sleep(self):
        print("sleep")

    def __iter__(self):
        return self

    def __next__(self):
        print("ahahah")
        return "ok"

b = A()

for i in b:
    print(i)