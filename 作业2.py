import random
l = []
i = 0
print("*"*20)
print("""
1.自动生成随机数字
2.手动输入数字
""")
m = input("请选择模式：")
if m=="1":
    while i<9:
        i+=1
        x = random.randint(-100,100)
        l.append(x)
elif m == "2" :
    i = 0
    while True:
        x = input("请输入数字")
        if not x:
            break
        l.append(x)
        i+=1
print(i)
print(l)
if i%2 == 0:
    print(max(l),min(l),l[(i//2)+1])
else:
    print(max(l), min(l), l[(i//2)])
l.sort(reverse=True)
print(l)
num =len(l)
m = ""
for x in range(num):
    ans = l[x]
    m = m+str(ans)+" "
print(m)
a = []
# while True:
#     str= input("请输入字符串:")
#     if not str:
#         break
#     a.append(str)
# print(a)
# a.sort(reverse=False)
# print(a)
# num = len(a)
# m =""
# for i in range(num):
#     ans = a[i]
#     m = m+ans+'\n'
# print(m)
#
