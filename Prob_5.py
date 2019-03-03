# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:34:26 2019

@author: Krozz
"""
#First Method
'''
def divn(x,n):
    for i in range(1,n+1):
        if x%i != 0:
            return False
    return True

res = 0

n = 20

temp = n
while temp>res:
    temp += n
    if divn(temp,n):
        res = temp
print(res)        
'''


#Second Method

num = 1
n = 10
a = list(range(1,n+1))
def remove(x,a):
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i*j == x:                
    return a.remove(i*j)                
print(num)    
