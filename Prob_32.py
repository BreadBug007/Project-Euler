import time

t1 = time.time()

def divn(num):
    l = []
    arr = [1,2,3,4,5,6,7,8,9]
    for i in range(2,int(num**0.5)+1):
        b = num%i
        if b == 0:
            rem = int(num/i)
            g = [int(i) for i in list(str(num) + str(rem) + str(i))]
            if len(g) == 9:
                res = [x for x in arr if x in g]                
                if len(res) == 9:
                    if num not in l:
                        l.append(num)
    return l


result = []
for i in range(1000,10000):
    req = divn(i)
    if len(req)>0:
        print(req)
        result+= req
        
print(sum(result))

t2 = time.time()
print(t2-t1)

'''def factors(n):
   return sorted(list(reduce(list.__add__,
               ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))'''