


import calendar
import time
t1 = time.time()
# Create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatyear(1900, w=2, l=1, c=6, m=3)
#print(str)

count = 0
for year in range(1901,2001):
    for month in range(1,13):
        res = calendar.monthrange(year, month)
        
        if res[0] == 1:
            count += 1
print(count)

t2 = time.time()

print(t2-t1)