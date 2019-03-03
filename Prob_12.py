# -*- coding: utf-8 -*-

'''import time

t1 = time.time()



tnum = 0
num = 1
count = 0
while count<6:
    count = 1
    tnum += num
    num += 1
    for i in range(1,int(tnum**0.5)+1):
        if tnum%i == 0:          
            count += 1


t2 = time.time()
print(tnum,count)
print(t2-t1)'''

import time
from math import sqrt


def count_divisors(n):
    d = {}
    count = 1

    while n % 2 == 0:
        n = n / 2
        try:
            d[2] += 1
        except KeyError:
            d[2] = 1

    for i in range(3, int(sqrt(n+1)), 2):
        while n % i == 0 and i != n:
            n = n / i
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1

    d[n] = 1

    for _,v in d.items():
        count = count * (v + 1)

    return count

def tri_number(num):
  next = 1 + int(sqrt(1+(8 * num)))
  return num + (next/2)


def main():
    i = 1
    while count_divisors(i) < 500:
        i = tri_number(i)
    return i


start = time.time()
answer = main()
elapsed = (time.time() - start)

print("result %s returned in %s seconds." % (answer, elapsed))





#-------------------------------------------------------------------------#



'''

import time


def num_divisors(n):
    if n % 2 == 0: n = n / 2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n / p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n + 1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n + 1)
    return n


start = time.time()
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2
elapsed = (time.time() - start)

print("result %s returned in %s seconds." % (triangle, elapsed))
'''