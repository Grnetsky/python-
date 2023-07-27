# import random
# import time
#
# def a():
#     c=0
#     while True:
#         c+=1
#         yield c  #有yield则是生成器
#
# def b():
#     b=1
#     while True:
#         b-=1
#         yield b
#
# def main():
#     i =0
#     a = time.time()
#     print(a)
#
# if __name__ == '__main__':
#     main()
a = 'abacbdfas'
for i in a:
    m = a.count(i)
    print(i,'的个数是',m)