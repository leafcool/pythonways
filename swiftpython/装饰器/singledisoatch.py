#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: singledisoatch.py 
@time: 2020/10/24 14:28 
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

# singledispatch
# 单分派泛函数：将多个函数绑定在一起组成一个泛函数，它可以通过参数类型将调用分派至其他函数上

from functools import singledispatch
import numbers

@singledispatch
def func(obj):
    print('object',obj)


# 只要可能，注册的专门函数应该处理抽象基类，不要处理具体实现（如 int）
@func.register(numbers.Integral)
def _(n):
    print('Integer', n)


# 可以使用函数标注来进行分派注册
@func.register
def _(s: str):
    print('String', s)


func(1)
func('test')
func([])


