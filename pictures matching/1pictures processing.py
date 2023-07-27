import os
import glob
from PIL import Image

def thumbnail_pic(path):
    #glob.glob(pathname)，返回所有匹配的文件路径列表
    a=glob.glob(r'F:/traffic technological match/*.jpg')
    for x in a:
        name=os.path.join(path,x)
        im=Image.open(name)
        im.thumbnail((800,600))
        print(im.format,im.size,im.mode)
        im.save(name,'JPEG')
    print('Done!')

if __name__=='__main__':
    path='F:\\traffic technological match'
    thumbnail_pic(path)
