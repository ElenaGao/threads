#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 6.守护线程.py
@date: 2020/7/14
"""
from threading import Thread
import time

"""
主线程运行结束之后不会立刻结束，会等待所有其他非守护线程结束才会结束
    因为主线程的结束意味着所在的进程结束
"""

# def task(name):
#     print(f'{name} is running')
#     time.sleep(1)
#     print(f'{name} is over')
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('haha',))
#     t.daemon = True
#     t.start()
#     print('主')


# 迷惑例子

import time


def foo():
    print(123)
    time.sleep(1)
    print('end123')


def func():
    print(456)
    time.sleep(3)
    print('end456')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=func)
    t1.daemon = True  # 123 456 主 end123 end456
    # t2.daemon = True  # 123 456 主 end123
    t1.start()
    t2.start()
    print('主')
