import time

t1 = time.time()

result = 0
rest = 200
for a in range(0, rest+1, 200):
    rest = 200 - a
    for b in range(0, rest+1, 100):
        rest = 200 - a - b
        for c in range(0, rest+1, 50):
            rest = 200 - a - b - c
            for d in range(0, rest+1, 20):
                rest = 200 - a - b - c - d
                for e in range(0, rest+1, 10):
                    rest = 200 - a - b - c - d - e
                    for f in range(0, rest+1, 5):
                        rest = 200 - a - b - c - d - e - f
                        for g in range(0, rest+1, 2):
                            h = 200 - a - b - c - d - e - f - g
                            if h >= 0:
                                result += 1
print(result)

t2 = time.time()

print(t2-t1)