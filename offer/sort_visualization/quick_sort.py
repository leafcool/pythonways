#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: quick_sort.py 
@time: 2020/10/20 12:04 
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
import copy
from .random_wait_sort import *

def quick_sort(data_set):
    frames = [data_set]
    ds = copy.deepcopy(data_set)

    def qsort(head, tail):
        if tail - head > 1:
        i = head
        j = tail - 1
        pivot = ds[j].value
        while i < j:
            if ds[i].value > pivot or ds[j].value < pivot:
                ds[i], ds[j] = ds[j], ds[i]
                frames.append(copy.deepcopy(ds))
            if ds[i].value == pivot:
                j -= 1
            else:
                i += 1
        qsort(head, i)
        qsort(i+1, tail)

    qsort(0, data_count)
    frames.append(ds)
    return frames
