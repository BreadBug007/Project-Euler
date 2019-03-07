import time

start = time.time()

def main():   
    d = {}
    for i in range(10000):
        s = str(''.join(sorted(str(i ** 3))))
        num_list = d.get(s, [])
        num_list.append(i)
        d[s] = num_list
        if len(num_list) == 5:
            return min(num_list) ** 3, num_list
        
print(main())

end = time.time()

print(end-start)