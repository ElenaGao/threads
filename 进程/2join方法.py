#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 2join方法.py
@date: 2020/7/13
"""
import time
from multiprocessing import Process


def task(name, n):
    print(f'{name} is running')
    time.sleep(n)
    print(f'{name} is over')


if __name__ == '__main__':
    # p1 = Process(target=task, args=('jason1', 1))
    # p2 = Process(target=task, args=('jason2', 2))
    # p3 = Process(target=task, args=('jason3', 3))
    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # # p.join()  # 主进程等待子进程运行结束之后再继续往后执行
    # print('主')


    start_time = time.time()
    p_list = []
    for i in range(1, 4):
        p = Process(target=task, args=('子进程%s' % i, i))
        p.start()
        p_list.append(p)

    for i in p_list:
        i.join()

    print('主', time.time() - start_time)
