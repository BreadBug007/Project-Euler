

import time
t1 = time.time()

def rec(n):
    value = 1
    l = []
    count = 0
    for k,i in enumerate(range(n)):
        if value%n != 0 and value%n not in l:
            count += 1
            value %= n
            l.append(value)
            value *= 10
    return count

max = 0
n = 1000

for j in range(n,1,-1):
    res = rec(j)
    if res > max:
        max = res
        num = j
    if max >= j-1:
        break
print("Number is",num,"and Recurrence is",max)

t2 =  time.time()

print(t2-t1)