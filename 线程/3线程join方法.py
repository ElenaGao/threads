#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 3线程join方法.py
@date: 2020/7/14
"""
import time
from threading import Thread


def talk(name):
    print(f'{name} is running')
    time.sleep(2)
    print(f'{name} is over')


if __name__ == '__main__':
    t = Thread(target=talk, args=('haha',))
    t.start()
    t.join()   # 线程阻塞，主线程等待子线程结束再执行
    print('主')

