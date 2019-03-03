import time
from itertools import permutations

t1 = time.time()

def divn(n):
    n = str(n)
    if int(n[7:10])%17 == 0:
        if int(n[6:9])%13 == 0:
            if int(n[5:8])%11 == 0:
                if int(n[4:7])%7 == 0:
                    if int(n[3:6])%5 == 0:
                        if int(n[2:5])%3 == 0:
                            if int(n[1:4])%2 == 0:                          
                                return True
            
    return False

def is_pandigital(nr, n):
    nr = str(nr)
    start=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(n)):
        if i not in start or i not in end:
            return False
    return True

result = 0

num = 1234567890

permutations = permutations(str(num))
values = [int(''.join(c)) for c in permutations if (''.join(c))[0] != '0']
tmid = time.time()
for i in values:
    if divn(i):
        print(i)
        result += i
print("Result is",result)            

t2 = time.time()    
print(t2-t1)
