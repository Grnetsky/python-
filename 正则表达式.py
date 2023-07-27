#coding = utf-8

import re

name = ['name1','-name','str']

for i in name:

    a = re.match(r'.*',i).group()

    print(a)

