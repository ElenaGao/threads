#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 5线程对象属性及其他方法.py
@date: 2020/7/14
"""
import time
from threading import Thread, active_count, current_thread
import os


def task():
    # print('hello world', os.getpid())
    print('hello world', current_thread().name)
    time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    t1.join()
    t.join()
    # print('主', os.getpid()) # 获取线程id9875
    # print('主', current_thread().name)   # 获取线程名 Thread-1 MainThread
    print('主', active_count())  # 统计正在活跃的线程数
