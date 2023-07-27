# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 18:54
# @Author  : Garnetsky
# @FileName: F.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
# a = [1,2,3,'b',{'b':1},'5',6]
# for i in a:
#     print(id(i))
# # 回型数

def circular(n):

    a =[]
    for i in range(n):
        x = [0 for i in range(n)]
        a.append(x)
    a[0] = [i+1 for i in range(n)]
    for index,x in enumerate(a) :
        if index !=0:
            x[n-1] = a[index-1][n-1]+1

    #     a[0] = [ i+1 for i in range(n)]
    #     for index,item in enumerate(a):
    #         item[n-1] = n+index
    # a[n - 1] = [2 * n + i - 1 for i in range(n)]

#     print(a)
#     for i in a:
#         print(i)
# circular(5)
#
# def m(*args,**kwargs):
#     print(args,kwargs)
#
# m(1,2,3,b=4,d=5)
# class father ():
#     def __init__(self,age):
#         self.age = age
#         self.name = 100
#         self.__sex = '男'
#     def eat(self):
#         print(self.name,'eat')
#         self.__sing()
#
#
#     def __sing(self):
#         print(self.name,'sing')
#
#     def test(self):
#         print(self.__sing())
#
# class child(father):
#     def c_test(self):
#         print(super(child, self))
#
#
# c = child(18)
# f = father(100)
# print(c.age,c.test())
