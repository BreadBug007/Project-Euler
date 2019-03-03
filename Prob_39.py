import time

t1 = time.time()

def count(p):
    poss = []
    if p%2 != 0:
        return 0
    else:
        count = 0
        for b in range(1,p//2):
            a = p/2 * ((p - 2*b)/(p - b))
            num = int(a)
            if a == num:
                val = tuple(sorted((num,b)))
                if val not in poss:
                    count += 1
                    poss.append(val)
        return count        

max = 0
for p in range(120,1000,2):
    value = count(p)
    if value > max:
        max = value
        val = p
print(val,count(val))

t2 = time.time()

print(t2-t1)