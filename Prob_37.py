import time

t1 = time.time()



def prime(n):
    n = int(n)
    if n == 1:
        return False
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def trunc(n):
    n = str(n)
    for i in range(len(n)-1):
        if not prime(int(n[:-i-1])):
            return False
        if not prime(int(n[i+1:])):
            return False
    return True

def even(n):
    n = str(n)
    for i in range(len(n)):
        if int(n[i])%2 == 0:
            return False
    return True
        
result = 23
count = 1
while count != 11:
    for i in range(13,1000000,20):
        if even(i) and prime(i) and trunc(i):
            count += 1
            result += i

    for j in range(17,1000000,20):
        if even(j) and prime(j) and trunc(j):
            count += 1
            result += j
            if count == 11:
                break
        

 
print(result)
 
t2 = time.time()

print(t2-t1)
