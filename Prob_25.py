
import time

t1 = time.time()

secondlast = 0
last = 1
for i in range(1,100000):
    result = last + secondlast
    secondlast = last
    last = result
    if len(str(result)) == 1000:
        print(i+1)
        break
t2 = time.time()
print(t2-t1)