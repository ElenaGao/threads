#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 4进程对象及其他方法.py
@date: 2020/7/13
"""
from multiprocessing import Process, current_process
import time
import os


def task():
    # print(f'{current_process().pid} is running') # 查看当前进程的进程号
    print('子', os.getpid())
    print(os.getppid())
    time.sleep(3)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()
    print('主', os.getpid())
    print('主主', os.getppid())
