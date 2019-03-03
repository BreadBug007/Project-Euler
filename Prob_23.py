

import time

t1 = time.time()

def divisor(n):
    sum = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            sum += i
            j = n//i
            if j>i:
                sum += j
    return sum
n = 28123
count = 0
num_list = []
for i in range(12,n):
    if divisor(i)>i:
        num_list.append(i)
count = sum(range(n+1))

d = {}
n2 = []
for k,i in enumerate(num_list):
   for j in num_list[k::]:
       if i+j not in d:
           if i + j < n+1 :        
               d[i+j] = i + j   
           else:
               break

print(count - sum(d))

t2 = time.time()

print(t2-t1)