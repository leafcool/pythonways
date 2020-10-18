#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: leafcool
@contact:598115455@qq.com
@version: 1.0.0
@license: Apache Licence
@file: ss.py
@time: 2020/10/15 21:25
"""
B = int(input())
if B < 1 or B > 1000:
    print("数据不符合题意")
elif B>=1 and B<=1000:
    for n in range(1,B):
        if n*(n-1)<2*B:
            if 2*B%n==0 and (2*B/n-n+1)%2==0:
                result=0
                a=(2*B/n-n+1)//2
                c=range(a,a+n)
                print('%d=%d' % (B,c[0]),end='')
                for i in range(1,len(c)):
                    print('+%d' % c[i],end='')
                if len(c)==0:
                    result+=1
print(result)





