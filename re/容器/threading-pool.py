#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: threading-pool.py 
@time: 2020/11/8 16:10 
@desc: 
'''
# code is far away from bugs with the god animal protecting
"""
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

from concurrent.futures import ThreadPoolExecutor
import threading,time
# def action(max):
#     my_sum=0
#     for i in range(max):
#         print(threading.current_thread().name+' '+str(i)+"\n")
#         my_sum+=1
#     return my_sum
# pool=ThreadPoolExecutor(max_workers=2)
# future1=pool.submit(action,50)
# future2=pool.submit(action,100)
# print(future1.done())
# time.sleep(1)
# print(future2.done())
# print(future1.result())
# print(future2.result())
# pool.shutdown()

# with ThreadPoolExecutor(max_workers=4) as pool:
#     result=pool.map(action,(20,100,120))
#     print('111111111111')
#     for i in result:
#         print(i)

# mydata=threading.local()
# def action(max):
#     for i in range(max):
#         try:
#             mydata.x+=i
#         except:
#             mydata.x=i
#         print('%s mydata.x:%d'%(threading.current_thread().name,mydata.x))
# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(action,10)
#     pool.submit(action,10)

# from threading import Timer
# import time
# count=0
# def time_t():
#     print("now time:%s"%time.time())
#     global t,count
#     count+=1
#     if count<10:
#         t=Timer(1,time_t)
#         t.start()
# t=Timer(3,time_t)
# t.start()
#
# import sched,time,threading
# s=sched.scheduler()
#
# def time_t(name='default'):
#     print('%s time %s'%(name,time.ctime()))
# print('main thread',time.ctime())
# s.enter(10,1,time_t)
# s.enter(5,2,time_t,argument=('location parameter',))
# s.enter(5,1,time_t,kwargs={'name':'key words'})
# s.run()
# print('main th',time.ctime())
#
# import os
# print(os.getpid())
# pid=os.fork()
# print(os.getpid())
# if pid==0:
#     print(os.getpid(),os.getppid())
# else:
#     print(os.getpid())
# print

import multiprocessing
#
# def f(q):
#     print('(%s) write data'%multiprocessing.current_process().pid)
#     q.put('python')
# if __name__ == '__main__':
#     q=multiprocessing.Queue()
#     p=multiprocessing.Process(target=f,args=(q,))
#     p.start()
#     print('(%s) show data'% multiprocessing.current_process().pid)
#     print(q.get())
#     p.join()

def f(conn):
    print('(%s) write data'%multiprocessing.current_process().pid)
    conn.send('python')
if __name__ == '__main__':
    parent_con,son_con=multiprocessing.Pipe()
    # q=multiprocessing.Queue()
    p=multiprocessing.Process(target=f,args=(son_con,))
    p.start()
    print('(%s) show data'% multiprocessing.current_process().pid)
    print(parent_con.recv())
    p.join()

