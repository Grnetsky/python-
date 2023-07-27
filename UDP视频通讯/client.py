# # -*- coding: utf-8 -*-
# # @Time    : 2022/3/30 16:27
# # @Author  : Garnetsky
# # @FileName: client.py
# # @Software: PyCharm
# # @Cnblogs ：http://blog.xroot.top
import socket
import struct
import cv2
import numpy


# 发送者
class videoTransfer():
    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.resolution = (640, 480)  # 分辨率
        self.img_fps = 95  # each second send pictures
        self.img = ''
        self.img_data = ''


    def send_vedio(self):
        camera = cv2.VideoCapture(0)
        img_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.img_fps]
        while True:
            _, self.img = camera.read()
            self.img = cv2.resize(self.img, self.resolution)
            _, img_encode = cv2.imencode('.jpg', self.img, img_param)
            img_code = numpy.array(img_encode)
            self.img_data = img_code.tobytes()
            try:
                print(self.img_data)
                self.udp_socket.sendto(b'123',('',8090))
            except Exception as err:
                print(err)
                camera.release()
                self.udp_socket.close()
                exit(0)
videoTransfer().send_vedio()

# import cv2
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 9999))
# cap = cv2.VideoCapture(1)
# cap.set(3, 320)
# cap.set(4, 240)
# while True:
#     data, addr = s.recvfrom(4096)
#     if data != '0':
#         _, fra = cap.read()
#         _, enfra = cv2.imencode('.jpg', fra)
#         s.sendto(enfra, ('127.0.0.1', 9999))
#     else:
#         s.close()
