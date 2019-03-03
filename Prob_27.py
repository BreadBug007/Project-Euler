

import time
from math import sqrt
t1 = time.time()

def func(a, b):
    check, n = True, 1
    while check:
        num = n*(n+a) + b
        if num > 0:
            if not prime(num):
                check = False
        else:
            break
        n += 1
    return n


def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

res, b = [0, 0, 0], []

for i in range(2,1000):
    if prime(i):
        b.append(i)
count = 1
        

for i in range(-999,1000,2):
    for j in b:
        if abs(i) <= j:
            seq = func(i, j)
            if seq > res[0]:
                res[0] = seq
                res[1] = i
                res[2] = j
                

print(res, res[1]*res[2])

t2 = time.time()

print(t2-t1)
    