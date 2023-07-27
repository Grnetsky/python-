import tkinter

address_list = dict()

w = tkinter.Tk()
w.title('手机联系人系统')
w.geometry('500x500')
w.geometry('+450+450')
w.mainloop()
print("")

def show_all():
    if not address_list:
        print("联系人为空")
    for key,value in address_list.items():

        print("联系人：", key, "的电话是：", value)

def del_name(name):

    if name not in address_list:

        print("查无此人")

    else:
        ans = int(input("确认删除吗，确认请按1，否认请按2:"))
        if ans == 1:
            del address_list[name]
            print("已成功删除")
        else:
            return

def clear():
    ans = int(input("确认要清除所有联系人吗（此操作无法撤回）确认请按1，否认请按2:"))

    if ans == 1:

        address_list.clear()

        print("清除成功")
    elif ans == 2:

        return

def add_change():
    name = input("请输入添加或修改联系人的名字：")

    num = input("请输入号码：")

    while not num.isdigit():

        num = input("请输入正确的号码:")

    else:

        address_list[name] = num

    print("操作成功")

def exit():
    print("欢迎下次使用，再见")

def main():
    print("*"*20+"手机联系人系统"+"*"*20)
    while True:
        print("1. 查询所有联系人")
        print("2. 添加联系人")
        print("3. 删除联系人")
        print("4. 修改联系人")
        print("5. 退出系统")
        print("6. 清除所有联系人")
        try:
            a = int(input("请输入要执行的操作："))
            if a == 2 or a == 4:
                add_change()
            elif a == 3:
                key = input("请输入要删除的联系人的名字：")
                del_name(key)
            elif a == 1:
                show_all()
            elif a == 5:
                exit()
                break
            elif a== 6:
                clear()
            else:
                print("无此选项，请重新输入")
        except Exception as ret:
            print("错误操作请重新输入")

if __name__ == '__main__':
    main()