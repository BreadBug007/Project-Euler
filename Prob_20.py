

import time 
t1 = time.time()

n = 100
fact = 1
for i in range(1,n):
    fact = fact*i    

a = map(int, str(fact))  

print(sum(a))  
t2 = time.time()  
print(t2-t1)