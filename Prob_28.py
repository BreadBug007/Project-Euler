
import time
t1 = time.time()

value_list = [1]
temp = 1
for i in range(3,1002,2):
    for j in range(temp+i-1,i*i+1,i-1):
        value_list.append(j)
    temp = j   
            
print(sum(value_list))

t2 = time.time()
print(t2-t1)