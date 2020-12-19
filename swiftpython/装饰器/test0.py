#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: test0.py 
@time: 2020/10/24 14:20 
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

# 开始实现装饰器
# 装饰器的典型行为：把被装饰的函数替换成新函数，二者接受相同的参数，而且（通常）返回被装饰的函数本该返回的值，同时还会做些额外操作
import time
from functools import wraps

def clock(func):
    @wraps(func)                         # 用 func 的部分标注属性（如 __doc__, __name__）覆盖新函数的值
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(t1 - t0)
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

snooze(1)