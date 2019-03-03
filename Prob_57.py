import time

start = time.time()

def num_and_den(n):
    num_old = 3
    den_old = 2
    iteration = 1
    for i in range(n-1):
        num_new = num_old + 2 * den_old
        den_new = num_new - den_old
        num_old = num_new
        den_old = den_new
        iteration += 1
    return num_new, den_new, iteration

count = 0
for i in range(2,1001):
    numerator, denominator, iteration = num_and_den(i)
    if len(str(numerator)) > len(str(denominator)):
        count += 1
print(count)    
    
end = time.time()
print(end-start)    