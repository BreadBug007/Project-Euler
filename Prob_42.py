from string import ascii_lowercase
import time

t1 = time.time()

opened_file = open('E:\Sharing\Data\p042_words.txt')
name_file = opened_file.read()
name_file = name_file.replace('"','')
name_list= name_file.split(',')
   
def tri(n):
    tri_list = []
    num = 0
    i = 1
    
    while i<=n:
        num = int(i*(i+1)/2)        
        if num not in tri_list:
            tri_list.append(num)
        i += 1
        
    return tri_list

tri_num = tri(20)


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text= str(text)
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)

name_value = []
for name in name_list:
    name_value.append(alphabet_position(name))

count = 0
for i in range(len(name_value)):
    value = name_value[i].split()
    temp = 0
    for j in value:
        temp += int(j)
    if temp in tri_num:
        count += 1
    
print(count)

            

t2 = time.time()    
print(t2-t1)