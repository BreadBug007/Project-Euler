import time
from itertools import permutations

t1 = time.time()

def is_prime(n):
    if n == 1:
        return False
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True


a = '123456789'
flag = True
j = 9

while flag:
    p = permutations(a[:j])
    p = list(p)[::-1]
    for i in p:
        number = int(''.join(i))
        if (number+1) % 6 == 0 or (number-1) % 6 == 0:
            if is_prime(number):
                print(number)
                flag = False
                break
    j -= 1
      
t2 = time.time()

print(t2-t1)
