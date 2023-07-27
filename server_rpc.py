# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 08:25
# @Author  : Garnetsky
# @FileName: server_rpc.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import time
from concurrent.futures import ThreadPoolExecutor

import grpc
import test_pb2_grpc
import test_pb2


# 补充服务端
# 补全调用的函数代码
class UserRecommends(test_pb2_grpc.UserRecommendServicer):
    def UserRecommend(self, request, context):
        """
        这是在接口中定义的用户推荐方法
        :param request: 调用时的请求参数对象
        :param context: 通过此对象可以设置调用返回的异常信息（ context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')）
        :return:
        """
        # 获取调用的参数（request = UserRequest   获取参数直接使用request.参数形式,并且数据类型就是python内置数据）
        channel_id = request.channel_id
        user_id = request.user_id
        article_num = request.article_num
        print(channel_id,user_id,article_num)
        # 返回参数(进行逻辑运算)
        rep = test_pb2.UserResponse()
        rep.exposer = 'exposure'
        rep.time_stamp = round(time.time() * 1000)
        # =使用extend方法
        _recommends = []
        for i in range(article_num):
            # 获取参数
            article = rep.Article()

            # 设置参数
            article.article_id = i + 1
            article.track.click = 'click param'
            article.track.collect = 'collect param'
            article.track.read = 'read param'

            # 写入数据
            _recommends.append(article)

        rep.recommends.extend(_recommends)

        #返回对象数据
        return rep
# 创建rpc服务器（固定代码）

def serve():
    """
    rpc服务端启动方法
    :return:
    """

    # 创建服务器(设置工作线程)
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    # 将自己实现的被调用实现方法与服务器绑定（使用pb2中的add_方法名_server(重写的类名()，服务器名)方法添加）
    test_pb2_grpc.add_UserRecommendServicer_to_server(UserRecommends(), server)
    # 绑定ip地址和端口
    server.add_insecure_port('127.0.0.1:8000')

    # 此方法为非阻塞代码 后面需要自己添加循环
    server.start()

    # 添加循环
    while True:
        time.sleep(10)


if __name__ == '__main__':
    serve()
