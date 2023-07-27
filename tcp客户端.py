import socket
import threading
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
tcp_client.bind(("",7878))
tcp_client.connect(("127.0.0.1",8001))
tcp_client
# tcp_client.sendto("123".encode("utf-8"),("127.0.0.1",8000))
#t
data = tcp_client.recvfrom(1024)
print(data[0].decode("utf-8"))
# def onmessageg():
#     pass
#
# while True:
#     msg = tcp_client.recv(1024).decode("utf-8")
#     print(msg)
#     send_msg = input("请输入：")
#     tcp_client.send(send_msg.encode("utf-8"))
#     threading.Thread(target=onmessageg)
#
