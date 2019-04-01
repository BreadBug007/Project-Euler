import time

start = time.time()


def npf(num):
    i = 2
    value = set()
    while i < num**0.5 or num == 1:
        if num % i == 0:
            num /= i
            value.add(i)
            i -= 1
        i += 1
    return len(value) + 1


j = 646

while True:
    if npf(j) == 4:
        j += 1
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    print(j-3)
                    break
    j += 1

end = time.time()
print(end-start)