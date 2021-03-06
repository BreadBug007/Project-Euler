import time

start = time.time()


def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

temp, total = 1, 1
num = 0
for i in range(3,30000,2):    
    for j in range(temp+i-1,i*i+1,i-1):
        total += 1
        if prime(j):
            num += 1 
    ratio = num / total
    temp = j 
    if ratio < 0.1:
        print(i)
        break

end = time.time()
print(end-start)