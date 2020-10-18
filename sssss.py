#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: leafcool
@contact:598115455@qq.com
@version: 1.0.0
@license: Apache Licence
@file: sssss.py
@time: 2020/10/15 23:02
"""
import sys

# for line in sys.stdin:
#     a = line.split()
#
#     # print(int(a[0]) + int(a[1]))

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        ID=values[0:3*n:3]
        id2=values[0:3*n:3]
def givemoney(ID0,id2,money):
    if id2==2:

        s = 15 * (money // 100)

    if id2==1:
        s =money+givemoney(ID0,id+1,money)

    if id2==0:
        givemoney(ID0,id2+2,money)







