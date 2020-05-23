#!/usr/bin/python3

# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_pal(n):
    s = str(n)
    l = len(s)
    pal = True
    for i in range(0, l//2):
        pal = pal and s[i] == s[l-1-i]
    return pal

max = 999
min = 100
out = 0
for i in range(max, min, -1):
    for k in range(max, min, -1):
        if is_pal(i*k):
            if i*k > out:
                out = i*k

print(out)