from math import sqrt
import re

for i in range(int(sqrt(1020304050607080900)), int(sqrt(1929394959697989990)), 10):
    if re.match('1.2.3.4.5.6.7.8.9.0', str(i * i)):
        print('Done', i)

    if i % 1000000 == 0:
        print(i)
