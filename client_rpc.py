# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 09:01
# @Author  : Garnetsky
# @FileName: client_rpc.py
# @Software: PyCharm
# @Cnblogs ：http://blog.xroot.top
import time
import grpc
import test_pb2
import test_pb2_grpc


def feed_articles(stub):
    """
    调用推荐系统
    :return:
    """
    # 获取request参数
    user_request = test_pb2.UserRequest()

    # 设置request参数
    user_request.user_id = 1
    user_request.channel_id = 2
    user_request.article_num = 10
    user_request.time_stamp = round(time.time()*1000)

    # 相当于在rpc中调用方法   返回为ret参数为UserResponse          rpc UserRecommend(UserRequest) returns (UserResponse) {}
    ret = stub.UserRecommend(user_request)
    print(ret)



def run():
    #  创建连接rpc服务器的对象
    with grpc.insecure_channel('127.0.0.1:8000') as channel:

        # 创建调用辅助工具对象 stub
        stub = test_pb2_grpc.UserRecommendStub(channel)

        # 可以通过stub进行rpc调用 stub.方法名     （方法名为在proto文件中 rpc所定义的方法名）

        # 实现业务逻辑
        feed_articles(stub)

if __name__ == '__main__':
    run()