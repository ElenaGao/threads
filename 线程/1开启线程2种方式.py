#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: 1开启线程2种方式.py
@date: 2020/7/13
"""

# 方式一
# import time
# from threading import Thread
#
#
# def task(name):
#     print(f'{name} is running')
#     time.sleep(1)
#     print(f'{name} is over')
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=('tom',))
#     t.start()
#     print('主')

# 方式二

from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print(f'{self.name} is running')
        time.sleep(1)
        print(f'{self.name} is over')


if __name__ == '__main__':
    t = MyThread('lala')
    t.start()
    print('主')
