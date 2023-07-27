from lxml import html
from typing import Union
tree = html.parse("1.html")
r = tree.xpath("/html/head/title")
print(r)

def a(keyword: Union[str,bytes,bytearray]):
    print(keyword)