#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 5守护进程.py
@date: 2020/7/13
"""
import time
from multiprocessing import Process


def task(name):
    print(f'{name} is alive')
    time.sleep(2)
    print(f'{name} is die')


if __name__ == '__main__':
    p = Process(target=task, args=('haha',))
    p.daemon = True  # 必须放在start()上面，随着主进程的结束而结束
    p.start()
    print('主')
