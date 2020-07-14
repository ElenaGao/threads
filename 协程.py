#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 协程.py
@date: 2020/7/14
"""
import time
from gevent import spawn
from gevent import monkey;monkey.patch_all()

"""
pip install gevent
gevent模块本身无法检测常见的一些io操作
在使用的时候需要额外导入
from gevent import monkey;monkey.patch_all()
"""


def heng():
    print('哼')
    time.sleep(2)
    print('哼哼')

def ha():
    print('哈')
    time.sleep(3)
    print('哈哈')

def hei():
    print('嘿')
    time.sleep(5)
    print('嘿嘿')


start_time = time.time()
g1 = spawn(heng)
g2 = spawn(ha)
g3 = spawn(hei)
g1.join()
g2.join()
g3.join()
print(time.time() - start_time)