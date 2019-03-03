# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:26:42 2019

@author: Krozz
"""
import time

import numpy as np

import random

start = time.time()
L = [[0]*21 for i in range(21)]

A = np.array(L, ndmin = 2)

A[20][20], A[0][0] = 1, 1
n = 20

d = {}

l = []

count = 0#while np.min(A) == 0:

v, h = 0, 0

for i in range(2*n):

   r = random.randint(1,2)

   if r == 1 and h < 20:

       h += 1

   elif v < 20:

       v += 1

   A[v][h] = 1
   end = time.time()
print(A)
print(end-start)