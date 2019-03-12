from time import time

start = time()


def phi(n) : 
    
    result = n 
    p = 2
    while(p * p <= n) : 
        
        if (n % p == 0) : 
            while (n % p == 0) : 
                n = int(n/p)
            result -= int(result/p)
        p += 1

    if (n > 1) : 
        result -= int(result/n)
   
    return result


def main():
    
    max = 0
    n = 1000000
    temp = 0
    
    for i in range(2, n+1, 2):       
        val = i / phi(i)
        if val > max:
            max = val
            temp = i
    return max, temp

print(main())


end = time()


print(end-start)