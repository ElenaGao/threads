#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 7进程间通信-队列.py
        队列Queue模块
        管道：subprocess
                stdin stdout stderr
        队列：管道+锁
              先进先出
        堆栈：先进后出
@date: 2020/7/13
"""

from multiprocessing import Queue

# 创建一个队列
q = Queue(5)

# 往队列中存数据
q.put(111)
q.put(222)
q.put(333)
print(q.full())  # 判断队列是否满
print(q.empty())  # 判断队列是否为空
q.put(444)
q.put(555)
print(q.full())
# q.put(666) # 当队列数据放满后，如果还有数据要存，程序会阻塞，直到有位置让出来

# 从队列中取数据
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
# v6 = q.get()  # 队列中如果已经没有数据的话，get方法会原地阻塞
# v6 = q.get_nowait()  # 没有数据直接报错_queue.Empty
# v6 = q.get(timeout=3)  # 没有数据等待timeout后再报错 _queue.Empty
print(v1, v2, v3, v4, v5)

"""
总结：
q.full()
q.empty()
q.get_nowait()
在多进程的情况下是不精确的

"""