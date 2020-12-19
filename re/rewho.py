#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: rewho.py 
@time: 2020/10/29 14:41 
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

# import re
# f=open('whodata.txt','r')
# for line in f:
#     print(re.split(r'\s\s+',line))
# f.close()

who="""['wesley', 'console', 'Jun 20 20:33\012']
['wesley', 'pts/9', 'Jun 22 01:38\011(192.168.0.6)\012']
['wesley', 'pts/1', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/2', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/4', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/3', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/5', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/6', 'Jun 20 20:33\011(:0.0)\012']
['wesley', 'pts/7', 'Jun 20 20:33\011(:0.0)\012']
[' wesley', 'pts/8', 'Jun 20 20:33\011(:0.0)\012']"""

import re,os
with os.popen(who,'r') as f:
    for line in f:
        print(re.split(r'\s\s+|\t',line.rstrip()))


