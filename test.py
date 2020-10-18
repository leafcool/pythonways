#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: leafcool
@contact:598115455@qq.com
@version: 1.0.0
@license: Apache Licence
@file: test.py
@time: 2020/10/14 22:35
"""
def gcd(a,b):
    while b:
        a,b=b,a%b
    return  a

def lcm(a,b):
    return  a*b//gcd(a,b)

while True:
    try:
        a,b=map(int,input().split())
        print(lcm(a,b))
    except:
        break
