#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 2实现TCP服务端并发的效果.py
@date: 2020/7/13
"""
import socket
from threading import Thread
from multiprocessing import Process

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8081))
server.listen(5)


# 将服务的代码单独封装成一个函数
def talk(conn):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break  # 针对linux客户端断开链接情况
            print(msg.decode('utf-8'))
            conn.send(msg.upper())
        except Exception as e:
            print(e)
            break
    conn.close()


if __name__ == '__main__':  # windows下start进程一定要写到这下面
    while True:
        conn, address = server.accept()  # 接客
        # 叫其他人来服务客户
        # t = Thread(target=talk, args=(conn,))
        t = Process(target=talk, args=(conn,))
        t.start()
