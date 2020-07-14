#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 协程实现TCP并发.py
@date: 2020/7/14
"""

import socket
from gevent import spawn
from gevent import monkey;

monkey.patch_all()


def communication(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionAbortedError as e:
            print(e)
            break
    conn.close()


def server(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        spawn(communication, conn)


if __name__ == '__main__':
    g1 = spawn(server, '127.0.0.1', 8080)
    g1.join()
