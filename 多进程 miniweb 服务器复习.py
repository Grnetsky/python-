import socket
import re
import multiprocessing
class WGSIsevice():
    def __init__(self,):
        self.sevice_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.sevice_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.sevice_socket.bind(("",7788))

        self.sevice_socket.listen()
def main():






if __name__ == '__main__':
    main()