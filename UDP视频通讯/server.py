# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 16:16
# @Author  : Garnetsky
# @FileName: server.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
# import socket
#
# udp_socket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udp_socket.bind(('',8090))
# while True:
#     recv_data = udp_socket.recvfrom(1024)
#     print(recv_data)
#
#
import cv2
import socket

port = 8090
host = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'1', (host, port))
cv2.namedWindow('img')
while True:
    data, addr = s.recvfrom(4000)
    if data:
        imde = cv2.imdecode(data, 1)
        cv2.imshow('img', imde)
        k = cv2.waitKey(1)
        if k == ord('q'):
            s.sendto(b'0', (host, port))
        break

s.close()

cv2.destroyAllWindows()
