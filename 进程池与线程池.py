#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 进程池与线程池.py
@date: 2020/7/14
"""
"""
任务提交方式：
    同步：提交任务之后原地等待任务的返回结果，期间不做任何事
    异步：提交任务之后不等待任务的返回结果，继续往下执行
          返回结果如何获取？？
          异步提交任务的返回结果，应该通过回调机制来获取
          回调机制：
            就相当于给每个异步任务绑定了一个定时炸弹，一旦该任务有结果立刻触发爆炸
"""


"""
总结：
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
    pool = ThreadPoolExecutor(5)  /  pool = ProcessPoolExecutor(5)
    pool.submit(task, i).add_done_callback(call_back)
    
"""

import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

pool = ThreadPoolExecutor(5)
# pool = ProcessPoolExecutor(5)


def task(n):
    print(n, os.getpid())
    time.sleep(2)
    return n ** n


def call_back(n):
    print('callback>>>', n.result())


if __name__ == '__main__':
    t_list = []
    for i in range(20):
        res = pool.submit(task, i).add_done_callback(call_back)  # 提交任务，异步提交，返回为Future对象
        t_list.append(res)  # result方法  同步提交

    # pool.shutdown()  # 关闭线程池，等待线程池中所有任务执行完毕
    # for t in t_list:
    #     print(">>>>>", t.result())  # 结果为有序
