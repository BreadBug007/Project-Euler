import time

start = time.time()



def check(n):
    n = int(n)
    count = 1
    x = [int(i) for i in str(n)]
    for i in range(2,7):
        num = [int(i) for i in str(n*i)]
        if set(x) != set(num):
            return False
    return count

for i in range(123456,166666):
    if check(i):
        print(i)
        break

end = time.time()

print(end-start)