import time
import itertools as it
import random
start = time.time()

def is_prime(n):
    n = int(n)
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def sieve(n):
    prime = [True]*n
    prime[0] = False
    prime[1] = False
    prime[2] = True
    
    for i in range(3, int(n**0.5)+1, 2):
        index = i * 2
        
        while index < n:
            prime[index] = False
            index += i
            
    prime_list = [2]
    
    for i in range(3, n, 2):
        if prime[i]:
            prime_list.append(i)
    return prime_list

def check(a,b):
    if is_prime(int(str(a) + str(b))) and is_prime(int(str(b)+ str(a))):
        return True
    return False

p = sieve(10000)

def prime_pair():
    for i,a in enumerate(p):
        for j,b in enumerate(p[i+1:],i+1):
            if check(a, b):
                for k,c in enumerate(p[j+1:],j+1):
                    if check(a,c) and check(b,c):
                        for l,d in enumerate(p[k+1:],k+1):
                            if check(a,d) and check(b,d) and check(c,d):
                                for m,e in enumerate(p[l+1:],l+1):
                                    if check(a,e) and check(b,e) and check(c,e) and check(d,e):
                                        return a,b,c,d,e

a,b,c,d,e = prime_pair()
print(a,b,c,d,e)
print(a+b+c+d+e)
end = time.time()

print(end-start)

















end = time.time()

print(end - start)