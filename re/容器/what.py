#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: what.py 
@time: 2020/11/15 12:29 
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
# with open('somefile.txt', 'w+', encoding='latin-1') as f:
    # print('Hello World!', file=f)

# import array
# nums = array.array('i', [1, 2, 3, 4])
# with open('data.bin','wb') as f:
#     f.write(nums)

# import os
# if not os.path.exists('somefile'):
#     with open('somefile','wt') as f:
#         f.write('Hello\n')
# else:
#     print('file already exist!')
#

# import os.path,string
#
# def read_into_buffer(filename):
#     buf=bytearray(os.path.getsize(filename))
#     with open(filename,'rb') as f:
#         f.readline(buf)
#     return buf
#
# with open('sample.bin','wb') as f:
#     f.write(b'hello world\n')
# buf=read_into_buffer('sample.bin')
# buf

# record_size = 32 # Size of each record (adjust value)
#
# buf = bytearray(record_size)
# with open('somefile', 'rb') as f:
#     while True:
#         n = f.readinto(buf)
#         if n < record_size:
#             break
#         # Use the contents of buf

import sys,io
sys.stdout.encoding
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding
print(sys.stdout.encoding)

