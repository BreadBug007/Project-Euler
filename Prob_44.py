import time

t1 = time.time()

def penta(n):
    penta_list = []
    num = 0
    i = 1    
    while i<=n:
        num = int(i*(3*i-1)/2)        
        if num not in penta_list:
            penta_list.append(num)
        i += 1        
    return penta_list

val = penta(5000)


def p_check(n):

    x = (1+(1+24*n)**0.5)/6

    return x == int(x)

count = 0
for i in val:
    if p_check(i):
        for j in val:
            if p_check(j):
                if j > i:
                    if p_check(j - i):
                        if p_check(j + i):
                            print(j-i)
                            count += 1
    if count == 1:
        break

t2 = time.time()

print(t2-t1)