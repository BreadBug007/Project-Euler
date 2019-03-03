import time

t1 = time.time()



def dec_to_bin(x):
    return int(bin(x)[2:])

def palin(n):
    if len(n) == 1:
        return True
    if n[0:] == n[::-1]:
        return True
    else:
        return False
        
result = 0  
for i in range(1,1000000,2):
    if palin(str(i)):
        bin_num = dec_to_bin(i)
        if palin(str(bin_num)):
            if i%2 != 0:
                result += i
print(result)

t2 = time.time()

print(t2-t1)
