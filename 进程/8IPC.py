#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 8IPC.py
@date: 2020/7/13
"""

"""
研究思路：
    1. 主进程和子进程借助于队列通信
    2. 子进程和子进程借助于队列通信
"""

# 主进程和子进程

# from multiprocessing import Queue, Process
#
#
# def producer(q):
#     q.put('我是23号技师 很高兴为您服务')
#     print('hello big baby')
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=producer, args=(q,))
#     p.start()
#     print(q.get())


# 子进程和子进程
#
# from multiprocessing import Queue, Process
#
#
# def producer(q):
#     q.put('我是23号技师 很高兴为您服务')
#
#
# def consumer(q):
#     print(q.get())
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=producer, args=(q,))
#     p1 = Process(target=consumer, args=(q,))
#     p.start()
#     p1.start()


import os
import time
import multiprocessing


# 向queue中输入数据的函数
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.asctime())
    queue.put(info)


# 向queue中输出数据的函数
def outputQ(queue):
    info = queue.get()
    print('%s%s\033[32m%s\033[0m' % (str(os.getpid()), '(get):', info))


# Main
if __name__ == '__main__':
    multiprocessing.freeze_support()
    record1 = []  # store input processes
    record2 = []  # store output processes
    queue = multiprocessing.Queue(3)

    # 输入进程
    for i in range(10):
        process = multiprocessing.Process(target=inputQ, args=(queue,))
        process.start()
        record1.append(process)

    # 输出进程
    for i in range(10):
        process = multiprocessing.Process(target=outputQ, args=(queue,))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    for p in record2:
        p.join()
