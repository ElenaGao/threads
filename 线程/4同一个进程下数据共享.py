#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 4同一个进程下数据共享.py
@date: 2020/7/14
"""

from threading import Thread
import time

money = 100


def task():
    global money
    money = 666


if __name__ == '__main__':
    t = Thread(target=task)
    t.start()
    t.join()
    print(money)
