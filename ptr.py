#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: test.py 
@time: 2021/6/10 16:42 
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


import random

"""建立一个随机字典用来验证代码"""
dict1={}  #使用字典K,V表示指针和其指向数值
n=random.randint(1,500) #设定数组一个随机长度
for i in range(n):
    dict1[i]=random.randint(0,100) #每个键值对赋随机值

# dict1={0:3,1:2,2:1,3:0,4:6}
# n=len(dict1)

"""计算移动一步后计算下一步指针移动最大范围区间m"""
def function(a,b):
    arr=[0]
    for i in range(a,b+1):
        # if dict1[i]+i-b>0:
            arr.append(dict1[i]+i-b)
    print(arr)
    return max(arr)  # return max positive shift

"""递归判断函数"""
def judgefunction(s1,s2):
    #判定s2指针能否覆盖到最后字典一位
    if s2>n-2:
        print("successfully go to the end of array")
    else:
        m=function(s1,s2)
        #m<1,无法正偏移量，说明此时结束
        if m<1:
            print("can't go to the array[n-1]")
        # m>1,有正偏移量，继续调用函数本身
        else:
                s1=s2
                s2+=function(s1,s2)
                return judgefunction(s1,s2)

s1=0
s2=dict1[0]
judgefunction(s1,s2)
