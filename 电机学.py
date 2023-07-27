import pytesseract,re
from decimal import Decimal
from PIL import Image

def main():
    imgae = Image.open('UDP视频通讯/res/1.png')

    contend = pytesseract.image_to_string(imgae) #文字识别模块 识别出数字

    print(contend)

    A = re.findall(r'\d{3,4}|\d{1,2} \d{3}',contend) #正则表达式 对数据进行处理

    B = Decimal('0.4') # 小数计算模块 字符串相加

    dict = {}

    for i in A:

        dict[B]=i

        B = B + Decimal('0.01')

        dict[Decimal('0.4')]='138'

        dict[Decimal('1.1')]='493'

    print(dict)
    W = 9.9e-4
    l = 0.3
    l2 = 0.5e-3
    N = 500
    A = 9e-4
    B0 = W/A
    U0 = 4*3.14e-7
    HFE = int(dict[Decimal(str(B0))])
    H0 = B0/U0
    print("磁场强度为",round(H0,1))
    F1 = HFE*l
    print("铁芯部分磁压降为",round(F1,1))
    F2 = H0*l2
    print("气隙部分磁压降为",round(F2,1))
    F = F1+F2
    print("磁动势为",round(F,1))
    I = F/N
    print("励磁电流为",round(I,2))

    while  True:
        C = str(input('请输入要查询的B值:'))

        result = Decimal(C)
        Final = {}
        try:
            Final = dict[result]

            print(Final)

        except KeyError:

            print('没有这个值')

if __name__ == '__main__':
    main()


