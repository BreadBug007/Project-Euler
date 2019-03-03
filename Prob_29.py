

import time

t1 = time.time()

def len_power(n):
    l = {}
    for i in range(2,n+1):
        for j in range(2,n+1):
            if i**j in l:
                l[i**j] += 1
            else:
                l[i**j] = 1
    return len(l)

print(len_power(100))

t2 = time.time()

print(t2-t1)