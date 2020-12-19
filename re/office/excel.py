#!/usr/bin/env python 
# encoding: utf-8 
''' 
@author: leafcool
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited. 
@contact: leafcool@live.com
@software: leafcool
@file: excel.py 
@time: 2020/10/30 12:55 
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
# class Role:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print("exe role objection")
# r=Role('manager')
# r()
# class Fib:
#     def __init__(self,len):
#         self.first=0
#         self.second=1
#         self.__len=len
#     def __next__(self):
#         if self.__len==0:
#             raise StopIteration
#         self.first,self.second=self.second,self.first+self.second
#         self.__len-=1
#         return self.first
#     def __iter__(self):
#         return self
#
#
# fib=Fib(10)
# print(next(fib))
# for el in fib:
#     print(el,end=' ')
#
# my_iter=iter([2,'fkit',4])
# print(my_iter.__next__())
# print(my_iter.__next__())

# class ValueDict(dict):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#     def getkeys(self,val):
#         result=[]
#         for key,value in self.items():
#             if value==val:result.append(key)
#         return result
#
# my_dict=ValueDict(chinese=88,math=99,english=98)
# print(my_dict.getkeys(88))
# my_dict['program']=88
# print(my_dict.getkeys(88))
#


# def test(val,step):
#     print('start')
#     cur=0
#     for i in range(val):
#         cur+=i*step
#         yield cur
#
# t=test(10,1)
# print(tuple(t))
#
#

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    # @property
    def setsize(self,size):
        self.width,self.height=size
    # @property
    def getsize(self):
        return self.width,self.height
    size=property(getsize,setsize)
    def __int__(self):
        return int(self.width*self.height)
    def __repr__(self):
        return 'rectangle(width=%g,height=%g)'%(self.width,self.height)

r=Rectangle(4,5)
print(int(r))


