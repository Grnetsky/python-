import tkinter

def hit_me():
    global on_hit

    if on_hit==False:
        var.set("you hitme")
        on_hit = True
    else:
        on_hit=False;
        var.set("别点了！")
def inser_point():

    var=entry.get()#返回内容

    t.insert('insert',var)#鼠标在哪就在那儿插入模式  如果想在定点上插入 则用行数.列数来替换'insert'

window = tkinter.Tk()

window.title("这是标题")

window.geometry("500x500")

window.geometry("+500+250")

window.resizable(0,0) # 设置为不可变尺寸

var = tkinter.StringVar() # 全局变量
# 设置标签
lb = tkinter.Label(window,textvariable=var,bg='red',fg='white',font=("",32),width=20,height=2)
# 设置点击变量（布尔）
on_hit=False

b = tkinter.Button(window,text="点击这里",width=15,height=2,command=inser_point)

lb.pack()

b.pack()


#show='*'将所有输入的内容转换为星号
entry = tkinter.Entry(window,show="*",)
entry.pack()

t =tkinter.Text(window,height=2)

t.pack()

window.mainloop()
