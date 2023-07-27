import pymysql

conn = pymysql.connect(host="localhost",user="root",password="WOAINI2000",database="lianxiren",charset="utf8")

couser = conn.cursor()

def change():

    name = input("请输入要修改的联系人姓名：")

    couser.execute("select name from xingming where name = '%s'" % name)

    if not couser.fetchall():
        print("查无此人")

    else:
        num = input("请输入新号码")

        while not num.isdigit:

            print("输入有误请重新输入")

        else:
            num = int(num)

            couser.execute("update xingming set num=%d where name = '%s'" % (num,name))

            conn.commit()

            print("修改完成")


def show_all():
    couser.execute("select * from xingming;")
    data = couser.fetchall()
    if  data:
        for name,num in data:
            print(name,"的电话为",num)
    else:
        print("联系人为空")

def del_name(name):
    couser.execute("select name from xingming where name='%s';" % name)

    if not couser.fetchall():
        print("查无此人")

    else:
        ans = int(input("确认删除吗，确认请按1，否认请按2:"))

        if ans == 1:
            couser.execute("delete from xingming where name='%s';" % name )

            conn.commit()

            print("已成功删除")

        else:
            return


def clear():
    ans = int(input("确认要清除所有联系人吗（此操作无法撤回）确认请按1，否认请按2:"))

    if ans == 1:

        print("清除成功")

    elif ans == 2:

        return


def add():
    name = input("请输入添加或修改联系人的名字：")

    num = input("请输入号码：")

    while not num.isdigit():

        num = input("请输入正确的号码:")

    else:
        num = int(num)

        couser.execute("insert into xingming value('%s',%d);" % (name,num))

        couser.execute("select * from xingming;")

        couser.fetchall()

        conn.commit()

    print("操作成功")


def exit():
    couser.close()

    conn.close()

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

            if a == 2:

                add()

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

            elif a == 4:

                change()

            else:

                print("无此选项，请重新输入")

        except Exception as ret:

            print("错误操作请重新输入",ret)

if __name__ == '__main__':
    main()