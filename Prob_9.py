# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:59:53 2019

@author: Krozz
"""
import time
t1 = time.time()
    
for a in range(1,1000):
    for b in range(a,1000):
        c = (a*a + b*b)**0.5
        if a+b+c == 1000:
            print(a*b*c)
t2 = time.time()
print(t2-t1)    