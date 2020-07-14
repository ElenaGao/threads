#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 3进程间数据隔离.py
@date: 2020/7/13
"""

from multiprocessing import Process

money = 100


def task():
    global money
    money = 666


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print(money)
