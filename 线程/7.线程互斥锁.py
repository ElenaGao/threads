#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 7.线程互斥锁.py
@date: 2020/7/14
"""
from threading import Thread, Lock
import time

money = 100
mutex = Lock()


def task(mutex):
    global money
    mutex.acquire()
    tmp = money
    time.sleep(0.1)
    money = tmp - 1
    mutex.release()


if __name__ == '__main__':
    t_list = []
    for i in range(100):
        t = Thread(target=task, args=(mutex,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print(money)
