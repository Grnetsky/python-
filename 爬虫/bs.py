from bs4 import BeautifulSoup

fp = open("./1.html", encoding="UTF-8")
soup = BeautifulSoup(fp, "lxml")
# print(soup.find_all(id="form"))  # 注意class下有下划线
# soup.tagName 返回的是第一个匹配的html标签
soup.select("div")[0].string

# string : 获取标签中直系的文本内容
# text : 获取标签中所有的文本内容
# 获取标签中的属性值 soup.select("div")[1]["class"]
print(soup.select("div")[2])