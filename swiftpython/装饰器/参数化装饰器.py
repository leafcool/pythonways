#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: 参数化装饰器.py 
@time: 2020/10/24 15:03 
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
#
# def counter(start=1):
#     def decorator(func):
#         n=start
#         def wrapped(*args,**kwargs):
#             nonlocal n
#             print(f'{func.__name__} called {n} times.')
#             n+=1
#             return func(*args,**kwargs)
#         return wrapped
#     return  decorator
#
# def test():
#     return
# t1 = counter(start=1)(test)
# t1()
# t1()
#
# @counter(start=2)
# def t2():
#     return
# t2()
# t2()
#

from decorator import decorator

@decorator
def counter(func, *args, **kwargs):
    if not hasattr(func, 'n'):
        func.n = 1
    print(f'{func.__qualname__} called {func.n} times.')
    retval = func(*args, **kwargs)
    func.n += 1
    return retval


@counter
def f(n):
    return n

# print(f(2))
print(f(3))