# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:05:34 2019

@author: Krozz
"""
n = 100000
list = []
for i in range(99000,n):
    for j in range(i,n):
        num = str(i*j)
        if (len(num) == len(str(n*n))-1) :
            num1= "".join(reversed(num))
            if (num == num1):
                list.append(num)
print(max(list))                
