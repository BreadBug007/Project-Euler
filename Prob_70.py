from time import time
import collections
start = time()

'''def phi(n) : 
    
    result = n 
    for i in p_list:
        if i*i > n:
            break
        if n%i == 0:
            n = int(n/i)
            result -= int(result/i)
        i += 1

    if (n > 1) : 
        result -= int(result/n)
   
    return result'''

def perm(m,n):
	n = collections.deque(str(n))
	for i in str(m):
		try:
			n.remove(i)
		except:
			return False
	return True

def sieve(n):
    
	n = int(n**0.5 + 1)
	p = [True]*(n+1)
	p[0] = p[1] = False
	s, i = [], 2
	while i <= n:
		if p[i]:
			s.append(i)
			for j in range(2*i,n+1,i):
				p[j] = False		
		i += 1		
	return s




def main(n):
    
    p_list = sieve(100000000)
    p_list = p_list[:500]
    res = [1000000000, 0]
    for k, i in enumerate(p_list):
        for j in p_list[k+1:]:
            count = i*j
            if count < n:
                phi = (i-1)*(j-1)
                if count / phi < res[0]:
                    if len(str(count)) == len(str(phi)) and perm(phi, count):
                        res[0] = count / phi
                        res[1] = count
    return res
    

print(main(10000000))


end = time()


print(end-start)