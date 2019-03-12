from time import time

#Referenced from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

start = time()

def ContFrac(S):
    m0 = 0
    d0 = 1
    a0 = int(S**0.5)  
    temp = a0
    i = 2
    while True:
        m1 = d0*a0 - m0
        d1 = (S - m1**2)/d0
        a1 = int((temp + m1)/d1)
        if a1 == 2*temp:
            return i%2 == 0
        m0 = m1
        d0 = d1
        a0 = a1
        i += 1


def main(N):
    count = 0
    for i in range(2, N+1):
        if i**0.5 != int(i**0.5):
            if ContFrac(i):
                count += 1
    return count
print(main(10000))



end = time()

print(end-start)