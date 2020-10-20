#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: binarySearch.py 
@time: 2020/10/20 14:33 
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

def binarySearch(arr,left,right,x):
    while left<=right:
        mid=int(left+(right-left)/2)# 找到中间位置。求中点写成(left+right)/2更容易溢出，所以不建议这样写
        if arr[mid]==x:
            print('found %d in index %d'%(x,mid))
            return mid
        elif arr[mid]<x:
            left=mid+1
            print('区间缩小到[%d %d]'%(mid+1,right))
        elif x<arr[mid]:
            right=mid-1
            print('区间缩小到[%d %d]' % (left,mid + 1))

    return -1

binarySearch([4,5,6,7,8,9,100],0,6,5)
binarySearch([4,5,6,7,10,20,100],0,6,4)

