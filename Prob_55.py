import time

start =  time.time()


def palin(n):
    if len(n) == 1:
        return True
    if n[0:] == n[::-1]:
        return True
    else:
        return False
    
def lych(n):
    num = n
    n = str(n)
    i = 0
    while i<50:
        n = str(int(n) + int(n[::-1]))
        if palin(n):
            return False
        i += 1
    if not palin(n):
        return num

counter = 0
for i in range(10000):
    if lych(i):
        print(lych(i))
        counter += 1
print(counter)

end = time.time()

print(end-start)