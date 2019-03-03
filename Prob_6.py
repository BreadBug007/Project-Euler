# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:27:33 2019

@author: Krozz
"""

import time

t1 = time.clock()

def square_sum(n):
    a = 0
    b = 0
    for i in range(1,n+1):
        a += i
        b += i*i
    return (a*a - b)

t2 = time.clock()


print(square_sum(100000000), t2-t1)