#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 2client.py
@date: 2020/7/14
"""
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8081))

while True:
    client.send(b'hello world')
    data = client.recv(1024)
    print(data.decode('utf-8'))
