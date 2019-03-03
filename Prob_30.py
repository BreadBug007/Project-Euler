

import time

t1 = time.time()

def func(n,a):
    res = 0
    for i in str(n):
        res += int(i)**a
    return res

result = 0

for i in range(2,354295):
    if i == func(i,5):
        result += i

print(result)

t2 = time.time()

print(t2-t1)