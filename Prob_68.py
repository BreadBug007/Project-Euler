
from collections import defaultdict
import itertools as it
from time import time

start = time()

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def seq(a, b):
    
    ring = [{10, a, b}]
    
    s = 10 + a + b
    
    d = defaultdict(lambda: 0)
    
    d[a] = 1
    d[b] = 1
    
    if s > 15:
        return
    
    for n in num[::-1]:
        for m in num:
            if n != m:
                temp = s - n - m
                
                if temp in num and temp != n and temp != m:
                    if {n, m} not in ring:
                        d[n] += 1
                        d[m] += 1
                        d[temp] += 1
                        if 3 not in d.values():   
                            ring.append({temp, n, m})
                            break
                        else:
                            d[n] -= 1
                            d[m] -= 1
                            d[temp] -= 1
    return ring


def series():
    
    for i in num:
        for j in num:
            temp = seq(i, j)
            if len(temp) == 5:
                return temp, 10 + i + j


def perm(n):
    return it.permutations(n)


def conc(n):
    val = [''.join(str(i)) for i in list(n)]
    val = ''.join(val)
    return val


res = ''


def main():
    
    ring = series()
    temp = sorted(ring[0][-1])[::-1]
    res = str(conc(temp))
    
    for i in range(4, 0, -1):
        
        val0 = sorted(ring[0][4-i])[::-1]
        val1 = sorted(ring[0][5-i])[::-1]
        print(val0,val1)
        for j in perm(val0):
            if j[-1] in val1 and j[0] == max(j):
                res += conc(j)
                
        if len(res) == 12:
            for j in perm(val1):
                if j[-1] in temp and j[0] == max(j):
                    res += conc(j)

    print(res)


main()
end = time()
print(end-start)
