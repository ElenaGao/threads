#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 多进程和多线程比较.py
@date: 2020/7/14
"""

"""
多线程是否有用要看具体情况
1. 单核：4个任务（IO密集型/计算密集型）
2. 多核：4个任务（IO密集型/计算密集型）
"""

# 计算密集型   每个任务都需要10s
"""
单核(实际场景中不用考虑，都是多核CPU)
    多进程：额外的消耗资源
    多线程：节约资源开销
多核
    多进程：总耗时 10s+
    多线程：总耗时 40s+
"""

# IO密集型   每个任务都需要10s
"""
多核
    多进程：相对浪费资源
    多线程：更加节省资源
"""
"""
总结：
    多进程和多线程都有各自优势，写项目时通常可以多进程下再开多线程
    既可以利用多核也可以节约资源消耗
"""


# 计算密集型
# from multiprocessing import Process
# from threading import Thread
# import os, time
#
#
# def work():
#     res = 0
#     for i in range(1, 10000000):
#         res *= i
#
#
# if __name__ == '__main__':
#     l = []
#     print(os.cpu_count())  # 获取计算机的CPU核数
#     start_time = time.time()
#     for i in range(12):
#         # p = Process(target=work)   # 0.96657395362854
#         p = Thread(target=work)   # 4.615729331970215
#         p.start()
#         l.append(p)
#
#     for p in l:
#         p.join()
#
#     print(time.time() - start_time)

# IO密集型

from multiprocessing import Process
from threading import Thread
import os, time


def work():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())  # 获取计算机的CPU核数
    start_time = time.time()
    for i in range(400):
        # p = Process(target=work)   # 46.24454474449158
        p = Thread(target=work)  # 2.389190912246704
        p.start()
        l.append(p)

    for p in l:
        p.join()

    print(time.time() - start_time)
