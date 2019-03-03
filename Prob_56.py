import time

start = time.time()

def power_sum(a,b):
    num_sum = sum([int(i) for i in str(a**b)])
    return num_sum

max_value = 0

for i in range(1,101):
    if i%10 != 0:
        for j in range(1,101):
            if j%10 != 0:
                value = power_sum(i,j)
                if value > max_value:
                    max_value = value
print(max_value)       

end = time.time()

print(end-start)    