#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 8. GIL全局解释器锁.py
@date: 2020/7/14
"""
"""
重点：
    1. GIL不是python的特点，而是CPython解释器的特点
    2. GIL是保证解释器级别的数据的安全
    3. GIL会导致同一个进程下的多个线程无法同时执行，即无法利用多核优势**********
    4. 针对不同的数据还是需要加不同的锁处理
    5. 解释型语言的通病：同一个进程下多个线程无法利用多核优势
"""

# GIL与普通互斥锁的区别
from threading import Thread, Lock
import time

mutex = Lock()
money = 100


def task(mutex):
    global money
    # 写法一
    # mutex.acquire()
    # tmp = money
    # time.sleep(0.1)
    # money = tmp - 1
    # mutex.release()

    # 写法二：
    with mutex:
        tmp = money
        time.sleep(0.1)   # 只要你进入IO了，GIL会自动释放
        money = tmp - 1


if __name__ == '__main__':
    t_list = []
    for i in range(100):
        t = Thread(target=task, args=(mutex,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    print(money)