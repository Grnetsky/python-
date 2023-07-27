import  random
se = random.randint(1,10)
temp=input('猜猜舟舟心里想的哪个数字，1-10之间哦：')
while not temp.isdigit():
   temp = input("输入错误，请重新输入：")
while int(temp) != se:
    if int(temp) > se:
        temp = input("大了大了，请重新输入")
        while not temp.isdigit():
            temp = input("输入错误请重新输入：")
    elif int(temp) < se:
        temp = input("小了小了，重新输入：")
        while not temp.isdigit():
            temp = input("输入错误请重新输入：")
print('哇，你是舟舟肚子里的蛔虫吗？')
print('猜中了也没有奖励')
print('游戏结束，不玩了')





