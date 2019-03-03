import time
t1 = time.time()
a = ''.join(str(i) for i in list(range(1,1000000)))


res = int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])
print(res)

t2 = time.time()

print(t2-t1)