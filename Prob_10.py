# -*- coding: utf-8 -*-


'''def prime_fn(n):
    primes = []
    for prime in range(2,n+1):
        isprime = True
        for num in range(2,int(prime**0.5)+1):
            if prime%num == 0:
                isprime = False
                break
        if isprime:
            primes.append(prime)
    return primes

prime_list = prime_fn(200000)
sum_prime = sum(prime_list)
print()'''

import time
t1 = time.time()
def sumPrimes(n):

   summ, sieve = 0, [True] * n

   for p in range(2, n):

       if sieve[p]:

           summ += p

           for i in range(p*p, n, p):

               sieve[i] = False

   return summ
print(sumPrimes(2000000))
t2 = time.time()
print(t2-t1)
