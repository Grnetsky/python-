# class Book(object):
#     def __init__(self, age):
#         self.__name = "ok"
#         self.age = age
#
#     def __show(self):
#         print("show了",self.__name)
#     def show(self):
#         self.__show()
#
# book1 = Book(100)
# book1.show()
# print(book1.age)
#
#
# import timeit
#
# timeit.timeit()
import socket
import cv2
import io
from PIL import Image
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(("0.0.0.0", 9090))
print("监听")
while True:
    data, IP = s.recvfrom(100000)
    print("来")
    bytes_stream = io.BytesIO(data)
    image = Image.open(bytes_stream)
    img = np.asarray(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # ESP32采集的是RGB格式，要转换为BGR（opencv的格式）
    cv2.imshow("ESP32 Capture Image", img)
    if cv2.waitKey(1) == ord("q"):
        break

