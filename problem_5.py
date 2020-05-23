#!/usr/bin/python3

# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

max = 1


for i in range(1, 21):
    
    if max % i != 0:
        print(i)
        max = max * i
        dev = 1
        for k in range(2, i):
            if i > k and i % k == 0:
                dev = k
        if dev: 
            max = max // dev

print(max)