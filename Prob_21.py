



import time
import timeit
t1 = time.time()

n = 10000

def divn(n):
    sums = {}
    sum = 1
    for j in range(2,int(n**0.5)+1):
        if n%j == 0:
            sum += j
            k = n//j
            if k>j:
                sum += k
    sums[n] = sum
    return sums

res = 0
for i in range(1,n):
    a = divn(i)
    a_new = a[i]
    b = divn(a_new)    
    for value in b:        
        if (b[value] in a and b[value] != value):            
            res += i
print(res)       

t2 = time.time()
print(t2-t1)