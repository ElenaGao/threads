#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 9生产者和消费者.py
@date: 2020/7/13
"""

from multiprocessing import Process, Queue, JoinableQueue
import time
import random


def producer(name, food, q):
    for i in range(5):
        data = f'{name}生产了{food}{i}'
        time.sleep(random.randint(1,3))
        print(data)
        q.put(data)


def consumer(name, q):
    while True:
        food = q.get()
        # if food is None:break
        time.sleep(random.randint(1, 3))
        print(f'{name}吃了{food}')
        q.task_done()  # 向q.join()发送一次信号，证明一个数据已经被取走了


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=('egon', '包子', q))
    p2 = Process(target=producer, args=('tank', '煲汤', q))
    c1 = Process(target=consumer, args=('jack', q))
    c2 = Process(target=consumer, args=('tom', q))
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    # q.put(None)
    q.join()  # 当计数器为0时，才往后运行
"""
JoinableQueue 每当你往该队列中存入数据时，内部会有一个计数器+1
每当你调用task_done的时候，计数器-1
q.join() 当计数器为0时，才往后运行
"""