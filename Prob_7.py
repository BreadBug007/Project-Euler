# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:04:07 2019

@author: Krozz
"""

import time
t1 = time.time()
def prime_fn(n):
    primes = []
    for prime in range(2,n+1):
        isprime = True
        for num in range(2,int(prime**0.5)+1):
            if prime%num == 0:
                isprime = False
                break
        if isprime:
            primes.append(prime)
        if len(primes)>10000:
            break
    return primes

prime_list = prime_fn(200000)

t2 = time.time()
print(prime_list[-1], t2-t1)