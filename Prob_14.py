
import time

t1 = time.time()

def seq(n, coll):    
    
    count = 1
    m = n
    while n > 1:
        if n%2 == 0:
            n  = int(n/2)
            if n in coll:
                count += coll[n]
                break    
            else:
                count += 1
        else:
            n = 3*n + 1
            if n in coll:
                count += coll[n]
                break
            else:
                count += 1
    coll[m] = count
    return count

def collatz(n):

   res = [1, 0]

   for i in range(1, n):

       m = seq(i, coll)

       if m > res[0]:

           res = [m, i]

   print(res)

coll = {}

collatz(1000000)
t2 = time.time()

print(t2-t1)