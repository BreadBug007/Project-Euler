import time
from itertools import permutations

start= time.time()

def prime(n):
    n = int(n)
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def perm(n):
    res = []
    perms = permutations(str(n))
    values = sorted([int(''.join(c)) for c in perms if (''.join(c))[0] != '0'])
    for val in values:
        if prime(val):
            res.append(val)
    return res

#value = perm(1486)
#print(value)

result = []
for l in range(1000,9999):
    value = perm(l)
    for i in value:
        for j in value:
            for k in value:
                if (k - j == j - i) and (k > j > i):
                    val = str(i) + str(j) + str(k)
                    if val not in result:
                        result.append(val)
print(result)
                    
end = time.time()

print(end-start)