#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 1开启进程的两种方式.py
@date: 2020/7/13
"""

# 第一种 常用

# from multiprocessing import Process
# import time
#
#
# def task(name):
#     print(f'{name} is running')
#     time.sleep(3)
#     print(f'{name} is over')
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=('jason',))
#     p.start()  # 告诉操作系统创建一个进程，异步
#     print('主')

# 第二种
import time
from multiprocessing import Process


class MyProcess(Process):
    def run(self) -> None:
        print('hello bf')
        time.sleep(2)
        print('get out')


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print('主')
