import time

start = time.time()

num = [i.strip().split() for i in open("Data\p067_triangle.txt").readlines()]

for i in range(len(num)):
    num[i] = [int(j) for j in num[i]]


def main():
    for i in range(len(num) - 2, -1, -1):
        for j in range(len(num[i])):
            num[i][j] = num[i][j] + max(num[i + 1][j], num[i + 1][j + 1])
    print(num[0][0])


main()
end = time.time()
print(end - start)
