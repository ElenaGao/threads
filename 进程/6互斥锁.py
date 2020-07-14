#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 6互斥锁.py
        多个进程操作同一份数据的时候，会出现数据错乱的问题
        针对上述问题，解决方式就是加锁处理：将并发变成串行，牺牲效率但保证了数据的安全
@date: 2020/7/13
"""
import json
import random
import time
from multiprocessing import Process, Lock


# 查票
def search(i):
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'用户{i}查询余票：{dic.get("ticket_num")}')


# 买票  1先查2再买
def buy(i):
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)

    # 模拟网络延迟
    time.sleep(random.randint(1, 3))

    if dic.get("ticket_num") > 0:
        dic['ticket_num'] -= 1
        with open('data', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f'用户{i}买票成功')
    else:
        print(f'用户{i}买票失败')


def run(i, mutex):
    search(i)
    # 2. 给买票环节加锁处理，抢锁
    mutex.acquire()
    buy(i)
    # 3. 释放锁
    mutex.release()


if __name__ == '__main__':
    # 1. 在主进程中生成一把锁，让所有子进程抢
    mutex = Lock()
    for i in range(1, 11):
        p = Process(target=run, args=(i, mutex))
        p.start()
