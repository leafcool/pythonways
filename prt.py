import random


"""建立一个随机数组用来验证代码"""
dict1={}  #使用字典K,V表示指针和其指向数值
n=random.randint(1,500) #假设数组变化个数
for i in range(n):
    dict1[i]=random.randint(0,10000) #每个数组的赋随机值


#计算移动一步后数组的K,V和b只计算下一步指针移动最大范围区间m
def function(a,b):
    arr=[]
    for i in range(a,b+1):
        arr.append(dict1[i]+i-b)
    return max(arr)  # return max positive shift

#递归函数判断
def judgefunction(s1,s2):
    m=function(s1,s2)
    if m<1:
            print("can't go to the array[n-1]")
    else:
            s1=s2
            s2+=function(s1,s2)
            if s2>n-2:
                print("successfully go to the end of array")
            else:
                return judgefunction(s1,s2)

s1=0
s2=dict1[0]
judgefunction(s1,s2)
