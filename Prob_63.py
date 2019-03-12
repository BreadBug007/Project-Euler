import time

start = time.time()

def power(n1,n2):
    
    num = n1 ** n2
    
    if len(str(num)) == n2:
        return True
    return False


def main():
    
    count = 0
    for i in range(1,25):
        for j in range(1,25):
            if power(i,j):
                count += 1
    return count

print(main())

end = time.time()

print(end-start)