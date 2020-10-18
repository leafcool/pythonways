#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: leafcool
@contact:598115455@qq.com
@version: 1.0.0
@license: Apache Licence
@file: k-neighbors.py
@time: 2020/9/29 23:23
"""

import  numpy as np
from sklearn import neighbors
knn=neighbors.KNeighborsClassifier()#get knn 分类器
data=np.array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
labels=np.array([1,1,1,2,2,2])
knn.fit(data,labels)
knn.predict([18,90])