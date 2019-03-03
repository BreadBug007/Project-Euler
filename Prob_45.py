import time

t1 = time.time()

def tri(n):
    tri_list = {}
    num = 0
    i = 1    
    while i<=n:
        num = int(i*(i+1)/2)        
        if num not in tri_list:
            tri_list[num] = i
        i += 1        
    return tri_list

def penta(n):
    penta_list = {}
    num = 0
    i = 1    
    while i<=n:
        num = int(i*(3*i-1)/2)        
        if num not in penta_list:
            penta_list[num] = i
        i += 1        
    return penta_list

def hexa(n):
    hex_list = {}
    num = 0
    i = 1    
    while i<=n:
        num = int(i*(2*i-1))        
        if num not in hex_list:
            hex_list[num] = i
        i += 1        
    return hex_list

t = tri(100000)

p =penta(100000)

h = hexa(100000)

temp = list(set(t).intersection(list(set(p).intersection(h))))
print(temp)
t2 = time.time()

print(t2-t1)
