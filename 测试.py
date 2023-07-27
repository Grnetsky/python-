num = [3,-8,-2,0,-1.5,-0.3,1.2]
num = input("请输入一组数字，以空格分开:")

num_list = num.split()
i = 0
num_dict = {}
ans_dict = {}
ans_sort = []
for num in num_list:
    num_dict[i]=num
    i+=1
for key,value in num_dict.items():
    ans = float(value)*float(value)
    ans_dict[key] = ans
ans_dict = sorted(ans_dict.items(),reverse=True,key=lambda x:x[1])
for sort in ans_dict:
    num = sort[0]
    num_order = num_dict[num]
    ans_sort.append(num_order)
a= ''
for x in ans_sort:
    a = a + x + ' '
print(a)


#
# num_dict_order = sorted(num_dict.items(),reverse=True,key=lambda x:x[1])
#
# print(num_dict_order)
