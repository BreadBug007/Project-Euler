from time import time

start = time()

def divn():
    second_last_num = 2
    second_last_den = 1
    last_num = 3
    last_den = 1
    count = 0
    for i in range(3,31):
        if i%3 == 0:
            count += 2
            num = count * last_num + second_last_num
            den = count * last_den + second_last_den
            second_last_num = last_num
            second_last_den = last_den
            last_num = num
            last_den = den
        else:
            num = last_num + second_last_num
            den = last_den + second_last_den
            second_last_num = last_num
            second_last_den = last_den
            last_num = num
            last_den = den
    return num


num_val = sum([int(i) for i in str(divn())])
print(num_val, divn())

end = time()

print(end-start)