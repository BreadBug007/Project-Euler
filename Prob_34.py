import time

t1 = time.time()

def fact(n):   
   f = 1
   for i in range(1,n+1):
       f *= i
   return f

num = [0,1,2,3,4,5,6,7,8,9]
d = {i:fact(i) for i in num}

   
ress = 0
for i in range(10,d[9]*7):
    num = i
    res = 0
    while num > 0:
        res += d[num%10]
        num //= 10
    if res == i:
        ress += i

print(ress)

t2 = time.time()
print(t2-t1)