#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: clockdeco_demo.py 
@time: 2020/10/24 15:50 
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
import time

def clock(func):
    def clocked(*args): # ➊
        t0 = time.perf_counter()
        result = func(*args) # ➋
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked #

# # clockdeco_demo.py
# import time
#
# @clock
# def snooze(seconds):
#     time.sleep(seconds)
# @clock
# def factorial(n):
#     return 1 if n < 2 else n*factorial(n-1)
# if __name__=='__main__':
#     print('*' * 40, 'Calling snooze(.123)')
#     snooze(.123)
#     print('*' * 40, 'Calling factorial(6)')
#     print('6! =', factorial(6))