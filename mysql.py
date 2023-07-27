import pymysql

#连接数据库
conn = pymysql.connect(host="localhost",port=3306,user='root',passwd='WOAINI2000',database='jing_dong')
#定义游标
cursor=conn.cursor()

def findall():
    cursor.execute("select * from goods")
def main():

    print("-"*50+"欢迎来到京东查询中心"+"-"*50)

    print("1.查询所有商品信息\n""2.查询所有品牌信息\n""3.查询所有类型信息\n")

    cmd = int(input("请输入要查询的类容：")) # input函数默认将内容转换为字符串

    if cmd==1:

        findall()

    elif cmd==2:

       pass
    else:
        pass


if __name__ == '__main__':
    main()



