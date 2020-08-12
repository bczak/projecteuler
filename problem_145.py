#!/usr/bin/python3

# How many reversible numbers are there below one-billion?

# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (10^9)?

count = 0
def is_digits_odd(n):
    for i in str(n):
        if int(i) % 2 == 0 : return False
    return  True
def reverse(n):
    return int(str(n)[::-1])

for k in range(1000000000):
    n = reverse(k)  
    if(len(str(k)) != len(str(n))): continue

    s = n+k
    if is_digits_odd(s): count += 1

print(count)