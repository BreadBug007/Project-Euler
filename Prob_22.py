
from csv import reader
from itertools import count
from string import ascii_lowercase
import timeit
import time
t1 = time.time()

opened_file = open('E:\Sharing\Data\p022_names.txt','r')
name_list =list(reader(opened_file))

def letter_indexes(text):
    text = text.lower()

    letter_mapping = dict(zip(ascii_lowercase, count(1)))
    indexes = [
      letter_mapping[letter] for letter in text 
      if letter in letter_mapping
    ]

    return ' '.join(str(index) for index in indexes)

for names in name_list:
    name_sort = sorted(list(names))
    name_list = []
    print(name_sort)
    for name in name_sort:
        name_list.append(letter_indexes(name))  
    result = 0
    for i in range(len(name_list)):
        value = name_list[i].split()
        print(value)
        temp = 0
        for j in value:
            temp += int(j)
            print(temp)
        result = result + temp*(i+1)
    print(result)

t2 = time.time()
print(t2-t1)
