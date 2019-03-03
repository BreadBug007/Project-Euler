import time

start = time.time()

def fact(n):
    if n == 0:
        return 1
    f = 1
    for i in range(2,n+1):
        f *= i
    return f


count = 0
for n in range(23,101):
    for r in range(1,n):
        val = fact(n)/(fact(r)*fact(n-r))        
        if val > 1000000:
            count += 1
            
print(count)

end = time.time()

print(end-start)