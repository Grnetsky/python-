import socket
import re
class WSGIserver(object):

    def __init__(self):

        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 重复使用socket
        self.socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        # bind绑定需要监听的ip和端口，ip一般是为了应对多ip地址（网卡）的设备，指定他监听哪个ip
        self.socket_server.bind(("",7890))

        self.socket_server.listen()

    def server_service(self):
        while True:

            # 第一个参数为socket对象，第二个参数为对方IP地址和端口
            new_socket, new_socket_addr =self.socket_server.accept() #阻塞
            print(new_socket,new_socket_addr)
            request = new_socket.recv(1024).decode("utf-8")

            request_lines = request.splitlines()

            print(request_lines)

            data = re.match(r'[^/]+(/[^ ]*)',request_lines[0]).group(1)

            print(data)
            send_data = "HTTP/1.1 200 OK\r\n"
            send_data += "\r\n"
            send_data+="ooo"
            if data == '/index.html' or data =='/':
                print("正在请求主页面")

                with open('./source/hhh.html','r') as f:
                    html_content = f.read()
                    print("已成功发送数据")

                send_data +='hhh'
                send_data +=html_content
                new_socket.send(send_data.encode("utf-8"))
                #with open('/index.html','w') as f:
            else:
                new_socket.send(send_data.encode("utf-8"))
            new_socket.close()



x = WSGIserver()
x.server_service()




