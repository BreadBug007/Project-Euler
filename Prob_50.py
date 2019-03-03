import time

t1 = time.time()

def is_prime(n):
    if n == 1:
        return False
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

def sieve(n):
    prime = [True]*n
    prime[0] = False
    prime[1] = False
    prime[2] = True
    
    for i in range(3,int(n**0.5)+1,2):
        index = i*2
        
        while index < n:
            prime[index] = False
            index += i
    prime_list = [2]
    
    for i in range(3,n,2):
        if prime[i]:
            prime_list.append(i)
    return prime_list

p = sieve(5000)


val = 0
p_list = []

for i in p:
    val += i
    if val >= 1000000:
        break
    p_list.append(val)
    
flag = True

while flag:
    if not is_prime(p_list[-1]):
        p_list[-1] -= p[0]
        p = p[1:]
    if is_prime(p_list[-1]):
        flag = False

      
print(p_list[-1], len(p_list))



t2 = time.time()
print(t2-t1)
        
            