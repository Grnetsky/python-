    import socket
    import multiprocessing

    def server_forever(new_socket):
        recv_data = new_socket.recv(1024).decode("utf-8")
        print(recv_data)



    def main():

        tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        tcp_server.bind(("", 8888))

        tcp_server.listen(128)

        while True:
            new_socket,new_socket_adres = tcp_server.accept()

            p = multiprocessing.Process(target=server_forever,args=(new_socket,))

            p.start()

            new_socket.close()



    if __name__ == '__main__':
        main()


