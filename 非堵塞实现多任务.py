import socket
tcp_service = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_service.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcp_service.bind(("",7788))

tcp_service.listen(128)

# 设置为非堵塞
tcp_service.setblocking(False)

client_list = list()
while True:

    try:
     new_client_socket,new_client_socket_addr=tcp_service.accept()

    except Exception:
        pass
    else:
        new_client_socket.setblocking(False)
        # 设置非阻塞

        print("一个新的客户端已连接",str(new_client_socket))

        client_list.append(new_client_socket)

    for client_socket in client_list:
        try:
            recv_data = new_client_socket.recv(1024)

            if recv_data:

                print(recv_data.decode("utf-8"))

            else:

                print("[%s]客户端已关闭" % str(new_client_socket))

                client_socket.close()

                client_list.remove(new_client_socket)

        except Exception:
            pass








