import itertools as it
import time
t1 = time.time()

def prime(n):
    n = str(n)
    if n!=str(5):
        ev = [int(i) for i in n]
        for k in ev:
            if (k%2 == 0 or k%5 == 0):
                return False
    n = [[n[i-j] for i in range(len(n))] for j in range(len(n))]
    for row in n:
        val = ''
        for j in row:
            val += j
        val = int(val)        
        for i in range(3,int(val**0.5)+1,2):
            if val%i == 0:
                return False
    return True


count = 1
for n in range(3,1000000,2):
    if prime(n):
        count += 1
        
print(count)

t2 = time.time()
print(t2-t1)