#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: client_协程.py
@date: 2020/7/14
"""
import socket
from threading import Thread, current_thread


def x_client():
    client = socket.socket()
    client.connect(('127.0.0.1', 8080))
    n = 0
    while True:
        msg = f'{current_thread().name} say hello {n}'
        n += 1
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))


if __name__ == '__main__':
    for i in range(200):
        t = Thread(target=x_client)
        t.start()
