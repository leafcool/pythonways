#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: leafcool
@contact:598115455@qq.com
@version: 1.0.0
@license: Apache Licence
@file: sss.py
@time: 2020/10/15 22:08
"""
n=int(input("请输入一个数字"))
n_sqrt=n**0.5
res=[]
def is_prime(s):
    if s<2:
        return False
    else:
        for i  in range(2,int(s**0.5)+1):
            if s%i==0:
                return False
                break
        else:
            return True


for j in range(2,int(n_sqrt)+1):
    t=n%j
    if t==0 and is_prime(j)==True and is_prime(n/j)==True:
        res.append(j)
        res.append(int(n/j))
        print(j,int(n/j))

if len(res)==0:
    print("-1 -1")
