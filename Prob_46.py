import time

start = time.time()



def prime(n):

    for i in range(3,int(n**0.5)+1,2):

        if n%i == 0:

            return False

    return True



def check(n):

    for i in p[::-1]:

        q = ((n-i)/2)**0.5

        if q == int(q):

            return True

    return False

    

p = []

    

def main():

    n = 1

    while True:

        n += 2

        if prime(n):

            p.append(n)

            continue

        if not check(n):

            return n



print(main())

        

end = time.time()

print(end-start)