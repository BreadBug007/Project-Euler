from itertools import permutations
import time

t1 = time.time()
perm = permutations([0,1,2,3,4,5,6,7,8,9])

count = 0
for i in perm:
    count += 1
    if count == 1000000:
        print(i)
    elif count > 1000000:
        break
    
t2 = time.time()

print(t2-t1)