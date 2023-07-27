import socket
import re
import multiprocessing
class WSGIservice(object):
    def __init__(self,service_address):#初始化
        self.listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        self.listen_socket.bind(service_address)
        self.listen_socket.setblocking(False) #设置为非堵塞方式
        self.listen_socket.listen(128)

    def client_service(self,client_socket):
            send_msg = "jjjjhhhhh"
            client_socket.send(send_msg.encode("utf-8"))


    def sevice_forever(self):

        while True:
            client_socket,client_address = self.listen_socket.accept()
            new_process = multiprocessing.Process(target=self.client_service,args=(client_socket,))
            new_process.start()

            print(client_address, "已连接")

            client_socket.close()

def main():
    service_address = ("",7788)
    a = WSGIservice(service_address)
    a.sevice_forever()

if __name__ == '__main__':
    main()