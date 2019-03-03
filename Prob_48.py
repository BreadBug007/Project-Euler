import time

t1 = time.time()


def power(n):
    return n**n

val = 0
for i in range(1,1001):
    val += power(i)
val = str(val)[::-1]
print(val[:10][::-1])

t2 = time.time()

print(t2-t1)