#! /usr/bin/python3
# coding:utf-8

"""
@version: 3.8
@author: elena
@file: server.py
@date: 2020/7/14
"""
import threading
import asyncio


@asyncio.coroutine
def hello():
    print(f'hello world {threading.current_thread()}')
    yield from asyncio.sleep(1)
    print(f'hello world {threading.current_thread()}')


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
